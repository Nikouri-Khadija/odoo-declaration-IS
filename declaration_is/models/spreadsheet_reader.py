# -*- coding: utf-8 -*-
import re
import logging

from odoo import _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

#  ID du template spreadsheet Odoo
SPREADSHEET_TEMPLATE_ID = 4

# ID tableau DGI → (nom feuille, token année N, token année N-1)
# Pour ajouter une nouvelle feuille, ajouter une ligne ici uniquement.
SHEET_CONFIG = {
    2: ("Bilan Actif",  "J1", "J2"),
    1: ("Bilan Passif", "H1", "H2"),
    6: ("CPC",          "J1", "J2"),
    
}

# Regex : détecte BALANCE_DOOSYS("514", J1/J2/H1/H2)
# Le token année est capturé génériquement ([A-Z]\d) pour supporter J1, J2, H1, H2, etc.
_RE_BALANCE = re.compile(
    r'(-?)\s*BALANCE_DOOSYS\(\s*["\']?(\d+)["\']?\s*,\s*([A-Z]\d)\s*\)',
    re.IGNORECASE,
)

# Regex : =SUM(C8:C10)
_RE_SUM = re.compile(
    r'^=?\s*SUM\(\s*([A-Z]+)(\d+)\s*:\s*([A-Z]+)(\d+)\s*\)\s*$',
    re.IGNORECASE,
)


class SpreadsheetReader:
    """
        # Bilan Actif  (id=3, tokens J1/J2)
        reader = SpreadsheetReader(env, year_n=2024, year_n1=2023, tableau_id=3)
        valeurs = reader.get_values(required_keys=MappingDGI.BilanActif)
    """

    def __init__(self, env, year_n: int, year_n1: int, tableau_id: int):
        self._env    = env
        self._year_n = int(year_n)
        self._year_n1 = int(year_n1)

        if tableau_id not in SHEET_CONFIG:
            raise ValidationError(
                _("Tableau DGI id=%d inconnu. Valeurs connues : %s")
                % (tableau_id, list(SHEET_CONFIG.keys()))
            )

        # les infos depuis SHEET_CONFIG
        sheet_name, self._token_n, self._token_n1 = SHEET_CONFIG[tableau_id]
        self._sheet_name = sheet_name

        self._raw_cells  = None 
        self._eval_cache = {}    
        self._bal_cache  = {}    

    # ── API publique ──────────────────────────────────────────────────────────

    def get_values(self, required_keys=None) -> dict:
        """
        Retourne { 'C8': 150000.0, 'D8': 0.0, ... } pour la feuille chargée.
        Les clés absentes de la feuille retournent 0.0.
        """
        self._load_sheet()

        keys = required_keys if required_keys is not None else self._raw_cells.keys()
        result = {}
        for key in keys:
            val = self._eval_cell(key) if key in self._raw_cells else None
            result[key] = 0.0 if val is None else val
        return result

    #  Chargement de la feuille ──────────────────────────────────────────────

    def _load_sheet(self):
        """Charge les cellules brutes depuis Odoo (une seule fois)."""
        if self._raw_cells is not None:
            return
        #on cherche la bonne spreadsheet en utilisant l'ID
        template = self._env.ref('balance_doosys.spreadsheet_rapports_bilan_cpc', raise_if_not_found=False)
        if not template or not template.exists():
            raise ValidationError(
                _("Template spreadsheet introuvable (ID=%d).") % SPREADSHEET_TEMPLATE_ID
            )
        #on cherche la bonne feuille en utilisaant sheet_name
        for sheet in template.spreadsheet_raw.get('sheets', []):
            if sheet.get('name') == self._sheet_name:
                #on sauvegarde ses cellules dans _raw_cells et on s'arrête.
                self._raw_cells = sheet.get('cells', {})
                _logger.info(
                    "SpreadsheetReader: %d cellules chargées depuis '%s'",
                    len(self._raw_cells), self._sheet_name,
                )
                return

        raise ValidationError(
            _("Feuille '%s' introuvable dans le spreadsheet.") % self._sheet_name
        )

    # ── Évaluation d'une cellule ──────────────────────────────────────────────

    def _eval_cell(self, key: str):
        """Retourne la valeur numérique d'une cellule (avec cache)."""
        if key in self._eval_cache:
            return self._eval_cache[key]

        cell    = self._raw_cells.get(key)
        content = str(cell.get('content', '')).strip() if cell else ''

        if not content:
            val = None
        elif not content.startswith('='):
            try:
                val = float(content.replace(',', '.').replace(' ', ''))
            except (ValueError, TypeError):
                val = None
        else:
            val = self._eval_formula(content, key)

        self._eval_cache[key] = val
        return val

    # ── Évaluation d'une formule ──────────────────────────────────────────────

    def _eval_formula(self, formula: str, key: str):
        """Détecte le type de formule et appelle le bon évaluateur."""

        # Référence inter-feuilles (ex: 'Feuil2'!C8) → on ignore
        if "'" in formula or '!' in formula:
            return None

        # 1. SUM
        m = _RE_SUM.match(formula)
        if m:
            col      = m.group(1)
            row_from = int(m.group(2))
            row_to   = int(m.group(4))
            
            total = 0.0
            for r in range(row_from, row_to + 1):
                v = self._eval_cell(f"{col}{r}")
                if v is not None:
                    total += v
            return total

        # 2. BALANCE_DOOSYS ────────────────────────────────────────────────────
        if 'BALANCE_DOOSYS' in formula.upper():
            return self._eval_balance(formula)

        # 3. Expression de cellules : =C7+D7, =C8+C11 ─────────────────────────
        return self._eval_expression(formula, key)

    def _eval_balance(self, formula: str):
        """
        Remplace chaque Balance_Doosys par sa valeur numérique
        """
        def replacer(m):
            sign  = m.group(1).strip()          # '' ou '-'
            prefix = m.group(2)
            token  = m.group(3).upper()         # J1, J2, H1, H2, ...

            
            if token == self._token_n1.upper():
             year = self._year_n1   # année N-1 = 2023
            else:
              year = self._year_n    # année N   = 2024
            val  = self._doosys_balance(prefix, year)
            return str(-val) if sign == '-' else str(val)

        expr = _RE_BALANCE.sub(replacer, formula.lstrip('='))
        return self._safe_eval(expr, formula)

    def _eval_expression(self, formula: str, current_key: str):
        """
        Remplace les références de cellules (C8, D10...) par leurs valeurs,
        puis évalue l'expression. 
        """
        expr = formula.lstrip('=').strip()
        refs = re.findall(r'[A-Z]+\d+', expr)

        if not refs:
            return self._safe_eval(expr, formula)

        for ref in sorted(set(refs), key=len, reverse=True):
            val  = 0 if ref == current_key else (self._eval_cell(ref) or 0)
            expr = expr.replace(ref, str(val))

        return self._safe_eval(expr, formula)
    

    @staticmethod
    def _safe_eval(expr: str, original: str):
        """Évalue une expression arithmétique simple. Aucune fonction Python autorisée."""
        try:
            return float(eval(expr))
        except Exception as e:
            _logger.warning("SpreadsheetReader: eval('%s') → %s", original, e)
            return None
    























































































    # ── Appel ORM doosys ─────────────────────────────────────────────────────

    def _doosys_balance(self, prefix: str, year: int) -> float:
        """Retourne débit − crédit pour un préfixe de compte (avec cache)."""
        cache_key = (prefix, year)
        if cache_key not in self._bal_cache:
            rows = self._env['account.account'].doosys_fetch_debit_credit([
                {'account_prefix': prefix, 'year': year}
            ])
            val = 0.0
            if rows:
                val = float(rows[0].get('debit', 0)) - float(rows[0].get('credit', 0))
            self._bal_cache[cache_key] = val
            _logger.debug("BALANCE_DOOSYS('%s', %d) = %.2f", prefix, year, val)
        return self._bal_cache[cache_key]
    

    
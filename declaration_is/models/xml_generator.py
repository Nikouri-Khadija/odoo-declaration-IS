# -*- coding: utf-8 -*-
import io
import zipfile
from xml.dom import minidom
from xml.etree import ElementTree as ET

from odoo import _
from odoo.exceptions import ValidationError

from .mapping_dgi        import MappingDGI
from .spreadsheet_reader import SpreadsheetReader
from .tableau_is         import BilanActif, BilanPassif, Cpc


class XmlGenerator:

    def __init__(self, env, company, date_debut_n, date_fin_n):
        self._env          = env
        self._company      = company
        self._date_debut_n = date_debut_n
        self._date_fin_n   = date_fin_n

        # Tableaux à générer
        self._tableau_bilan_actif  = BilanActif()
        self._tableau_bilan_passif = BilanPassif() 
        self._tableau_cpc          = Cpc()

        self._xml_bytes = None

    # ── Point d'entrée principal ──────────────────────────────────────────────

    def build(self) -> bytes:
        self._load_and_fill_tableaux()
        self._generate_xml()
        return self._generate_zip()

    # ── Chargement et remplissage des tableaux ────────────────────────────────

    def _load_and_fill_tableaux(self):
        year_n  = self._date_debut_n.year
        year_n1 = year_n - 1

        self._fill_tableau(self._tableau_bilan_actif,  MappingDGI.BilanActif,  year_n, year_n1)
        self._fill_tableau(self._tableau_bilan_passif, MappingDGI.BilanPassif, year_n, year_n1)
        self._fill_tableau(self._tableau_cpc,          MappingDGI.Cpc,         year_n, year_n1) 

    def _fill_tableau(self, tableau, mapping: dict, year_n: int, year_n1: int):
        """
        Charge les valeurs depuis le spreadsheet pour un tableau donné,
        puis remplit le tableau avec le mapping DGI.
        """
        reader = SpreadsheetReader(
            env        = self._env,
            year_n     = year_n,
            year_n1    = year_n1,
            tableau_id = tableau.id_tableau,  
        )
        valeurs = reader.get_values(required_keys=mapping)
        tableau.remplir_valeurs(valeurs, mapping)

    # ── Génération XML ────────────────────────────────────────────────────────

    def _generate_xml(self) -> bytes:
        identifiant_fiscal = (
            self._company.identifiant_fiscal
           
        )

        root   = ET.Element('Liasse')
        modele = ET.SubElement(root, 'modele')
        ET.SubElement(modele, 'id').text = '6'

        resultat = ET.SubElement(root, 'resultatFiscal')
        ET.SubElement(resultat, 'identifiantFiscal').text = identifiant_fiscal
        ET.SubElement(resultat, 'exerciceFiscalDu').text  = self._date_debut_n.strftime('%Y-%m-%d')
        ET.SubElement(resultat, 'exerciceFiscalAu').text  = self._date_fin_n.strftime('%Y-%m-%d')

        groupe = ET.SubElement(root, 'groupeValeursTableau')
        groupe.append(self._tableau_bilan_actif.to_xml())
        groupe.append(self._tableau_bilan_passif.to_xml())
        groupe.append(self._tableau_cpc.to_xml())

        raw      = ET.tostring(root, encoding='utf-8', xml_declaration=True)
        reparsed = minidom.parseString(raw)
        self._xml_bytes = reparsed.toprettyxml(indent='  ', encoding='utf-8')
        return self._xml_bytes

    # ── Génération ZIP ────────────────────────────────────────────────────────

    def _generate_zip(self) -> bytes:
        if self._xml_bytes is None:
            raise ValidationError(
                _("_generate_xml() doit être appelé avant _generate_zip().")
            )
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zf:
            zf.writestr(self.xml_filename, self._xml_bytes)
        return buf.getvalue()

    @property
    def xml_filename(self) -> str:
        return (
            f"liasse_IS_"
            f"{self._company.identifiant_fiscal}_"
            f"{self._date_debut_n.year}.xml"
        )

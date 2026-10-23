# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class DeclarationIsHistory(models.Model):
    _name = 'declaration.is.history'
    _description = 'Historique des déclarations IS'
    _order = 'date_generation DESC'

    company_id = fields.Many2one(
        'res.company',
        string='Société',
        required=True,
        ondelete='cascade'
    )
    annee_exercice = fields.Char(
        string='Année exercice',
        required=True,
        help="Année de l'exercice fiscal (ex: 2024)"
    )
    date_generation = fields.Date(
        string='Date de génération',
        default=fields.Date.today,
        required=True
    )
    statut = fields.Selection(
        selection=[
            ('draft', 'Brouillon'),
            ('generated', 'Générée'),
        ],
        string='Statut',
        default='generated',
        required=True
    )
    xml_filename = fields.Char(string='Nom du fichier XML')
    zip_attachment_id = fields.Many2one(
        'ir.attachment',
        string='Fichier ZIP',
        ondelete='set null'
    )

    def name_get(self):
        result = []
        for rec in self:
            name = f"{rec.company_id.name} - {rec.annee_exercice} ({rec.date_generation})"
            result.append((rec.id, name))
        return result

    def action_download_zip(self):
        """Télécharger à nouveau le fichier ZIP associé."""
        self.ensure_one()
        if not self.zip_attachment_id:
            raise UserError(_("Aucun fichier ZIP associé à cette déclaration."))
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{self.zip_attachment_id.id}?download=true',
            'target': '_self',
        }
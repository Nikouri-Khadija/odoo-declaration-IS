# -*- coding: utf-8 -*-

import base64

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta

from ..models.xml_generator import XmlGenerator


class DeclarationIsWizard(models.TransientModel):
    _name = 'declaration.is.wizard'
    _description = 'Assistant de Déclaration IS'

    company_id = fields.Many2one(
        'res.company',
        string='Société',
        required=True,
        default=lambda self: self.env.company,
    )
    date_debut_n = fields.Date(
        string='Date de début N',
        required=True,
        default=lambda self: fields.Date.today().replace(month=1, day=1),
    )
    date_fin_n = fields.Date(
        string='Date de fin N',
        required=True,
        default=lambda self: fields.Date.today().replace(month=12, day=31),
    )
    date_debut_n1 = fields.Date(
        string='Date début N-1',
        compute='_compute_periode_n1',
        readonly=True,
    )
    date_fin_n1 = fields.Date(
        string='Date fin N-1',
        compute='_compute_periode_n1',
        readonly=True,
    )

    @api.depends('date_debut_n', 'date_fin_n')
    def _compute_periode_n1(self):
        for rec in self:
            if rec.date_debut_n and rec.date_fin_n:
                rec.date_debut_n1 = rec.date_debut_n - relativedelta(years=1)
                rec.date_fin_n1 = rec.date_fin_n - relativedelta(years=1)
            else:
                rec.date_debut_n1 = rec.date_fin_n1 = False

    @api.constrains('date_debut_n', 'date_fin_n')
    def _check_dates(self):
        for rec in self:
            if rec.date_fin_n < rec.date_debut_n:
                raise UserError(
                    _("La date de fin doit être postérieure à la date de début.")
                )

    def action_generer_declaration(self):
        self.ensure_one()

        if not self.company_id.identifiant_fiscal:
            raise UserError(
                _("L'Identifiant Fiscal (IF) de la société « %s » n'est pas renseigné.")
                % self.company_id.name
            )

        # ── Pipeline complet via XmlGenerator
        gen = XmlGenerator(
            env=self.env,
            company=self.company_id,
            date_debut_n=self.date_debut_n,
            date_fin_n=self.date_fin_n,
        )
        zip_data     = gen.build()
        xml_filename = gen.xml_filename
        zip_filename = xml_filename.replace('.xml', '.zip')

        # ── Attachement Odoo
        attachment = self.env['ir.attachment'].create({
            'name':      zip_filename,
            'type':      'binary',
            'datas':     base64.b64encode(zip_data),
            'res_model': self._name,
            'res_id':    self.id,
            'mimetype':  'application/zip',
        })

        # ── Historique
        self.env['declaration.is.history'].create({
            'company_id':        self.company_id.id,
            'annee_exercice':    str(self.date_debut_n.year),
            'date_generation':   fields.Date.today(),
            'statut':            'generated',
            'xml_filename':      xml_filename,
            'zip_attachment_id': attachment.id,
        })

        return {
            'type':   'ir.actions.act_url',
            'url':    f'/web/content/{attachment.id}?download=true',
            'target': '_self',
        }
# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_category_id = fields.Many2one(comodel_name="res.partner.category", string="Category", required=False, )
    delivery_company = fields.Boolean(string="Delivery Company", default=False)
    financial_file = fields.Char(string="Financial File", required=False, )

    @api.onchange('is_company')
    def _reset_delivery_company(self):
        if not self.is_company:
            self.delivery_company = False

    _sql_constraints = [
        (
            "ref_uniq",
            "unique(ref)",
            "Partner Reference must be unique across the database!",
        )
    ]

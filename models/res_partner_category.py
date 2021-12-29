# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError


class PartnerCategory(models.Model):
    _name = 'res.partner.category'
    _description = "Partner Category"
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name', index=True, required=True)
    complete_name = fields.Char('Complete Name', compute='_compute_complete_name', store=True)
    parent_id = fields.Many2one('res.partner.category', 'Parent Category', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('res.partner.category', 'parent_id', 'Child Categories')
    partner_count = fields.Integer(
        '# partners', compute='_compute_partner_count',
        help="The number of partners under this category (Does not consider the children categories)")

    discount_cash = fields.Boolean(string="Cash Discount", tracking=True, )
    discount_type = fields.Selection([('percent', 'Percentage'), ('amount', 'Amount')], string='Discount type',
                                     default='percent', tracking=True, )
    discount_cash_value = fields.Integer(string="Discount Value", digits=(6, 0), tracking=True, )

    discount_extra = fields.Boolean(string="Extra Discount", tracking=True, )
    discount_extra_type = fields.Selection(string="Extra Discount Type",
                                           selection=[('1', 'Fixed'), ('2', 'Levels'), ('3', 'Rate'), ],
                                           required=False, tracking=True, )
    discount_extra_value = fields.Integer(string="Discount Value", digits=(6, 0), tracking=True, )

    discount_commercial = fields.Boolean(string="Commercial Discount", tracking=True, )
    discount_commercial_type = fields.Selection([('percent', 'Percentage'), ('amount', 'Amount')], string='type',
                                                default='percent', tracking=True, )
    discount_commercial_value = fields.Integer(string="Discount Value", digits=(6, 0), tracking=True, )

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name

    def _compute_partner_count(self):
        read_group_res = self.env['res.partner'].read_group([('categ_id', 'child_of', self.ids)], ['categ_id'],
                                                            ['categ_id'])
        group_data = dict((data['categ_id'][0], data['categ_id_count']) for data in read_group_res)
        for categ in self:
            partner_count = 0
            for sub_categ_id in categ.search([('id', 'child_of', categ.ids)]).ids:
                partner_count += group_data.get(sub_categ_id, 0)
            categ.partner_count = partner_count

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive categories.'))
        return True

    @api.model
    def name_create(self, name):
        return self.create({'name': name}).name_get()[0]

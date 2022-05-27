# -*- coding: utf-8 -*-


from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    sale_order_approval_rule_id = fields.Many2one('sale.order.approval.rule', string='Sale Order Approval Rules')
    sale_order_approval = fields.Boolean(string='Sale Order Approval By Rule')

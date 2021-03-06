# -*- coding:utf-8 -*-
from odoo import fields, models, api


class MrpBOM(models.Model):
    _inherit = 'mrp.bom'

    label = fields.Char(string='Label')
    drawing = fields.Char(string='Drawing')
    non_standard_bom = fields.Boolean(related='product_tmpl_id.non_standard_bom', string='Not having Standard BOM')
    bom_dummy_id = fields.Many2one('bom.dummy', string='Dummy BOM')
    dummy_bom_state = fields.Selection(related='bom_dummy_id.state', string='BOM Dummy State')
    non_standard_bom = fields.Boolean(related='product_tmpl_id.non_standard_bom', string='Not having Standard BOM')
    routing_id = fields.Many2one('mrp.routing', string='Routing')
    line_no = fields.Char(string="Line No")


class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    qty_available = fields.Float(related='product_id.qty_available', string='On Hand', readonly=True)
    qty_reserve = fields.Float(related='product_id.outgoing_qty', string='Reserved')
    purchase_price = fields.Float(string='Purchase Price', compute='get_purchase_price')
    product_value = fields.Float(string='Stock Value', compute='get_stock_value')

    @api.depends('product_id')
    def get_purchase_price(self):
        for line in self:
            price = 0.0
            if line.product_id and line.product_id.id and isinstance(line.product_id.id, int):
                price = line.product_id.standard_price or 0.0
            line.purchase_price = price or 0.0

    @api.depends('product_id')
    def get_stock_value(self):
        for line in self:
            value = 0.0
            if line.product_id and line.product_id.id and isinstance(line.product_id.id, int):
                self._cr.execute('select sum(value) as value from stock_valuation_layer where product_id=%s;'%(line.product_id.id))
                result = self._cr.dictfetchall()
                value = result and result[0] and result[0].get('value')
            line.product_value = value or 0.0

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

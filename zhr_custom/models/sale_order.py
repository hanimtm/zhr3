from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    contact_id = fields.Many2one(comodel_name='res.partner', string='Contact')

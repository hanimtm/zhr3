from odoo import fields, models, api, _


class SalaryRulesInherit(models.Model):
    _inherit = 'hr.salary.rule'

    journal = fields.Boolean('New Journal')
    journal_id = fields.Many2one(comodel_name='account.journal', string='Journal')

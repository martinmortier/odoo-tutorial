from odoo import models, exceptions


class EstateAccount(models.Model):
    _inherit = 'estate.property'

    def action_sold(self):
        return super().action_sold()
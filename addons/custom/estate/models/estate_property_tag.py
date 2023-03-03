from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name='estate.property.tag'
    _order = 'name desc'

    name = fields.Char(required=True)

    _sql_constraints = [
        ('check_name', 'UNIQUE(name)', 'Tag must be unique')
    ]
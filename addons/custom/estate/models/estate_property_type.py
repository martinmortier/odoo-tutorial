from odoo import models,fields

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'

    name = fields.Char(required=True)

    _sql_constraints = [
        ('check_name', 'UNIQUE(name)', 'Tag must be unique')
    ]

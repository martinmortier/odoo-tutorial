from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'

    name = fields.Char(required=True)

    property_ids = fields.One2many('estate.property', 'property_type_id')

    _sql_constraints = [
        ('check_name', 'UNIQUE(name)', 'Tag must be unique')
    ]

from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _order = 'sequence, name'

    name = fields.Char(required=True)
    sequence = fields.Integer('Sequence', default=1)

    property_ids = fields.One2many('estate.property', 'property_type_id')

    _sql_constraints = [
        ('check_name', 'UNIQUE(name)', 'Tag must be unique')
    ]

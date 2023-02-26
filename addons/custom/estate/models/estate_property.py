from odoo import models,fields

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=fields.Date.add(fields.Date.today(), months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection(string='Type',selection=[('north','North'), ('south','South'), ('east','East'), ('west','West')])
    active = fields.Boolean(default=True)
    state = fields.Selection(default='new',required=True,copy=False,selection=[('new','New'), ('offer_received','Offer Received'), ('offer_accepted','Offer Accepted'), ('sold','Sold'), ('canceled','Canceled')])
    property_type_id = fields.Many2one('estate.property.type', string='Property type')
    sales_person_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    tag_ids = fields.Many2many('estate.property.tag')
    offer_ids = fields.One2many('estate.property.offer', 'property_id')

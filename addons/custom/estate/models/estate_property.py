from odoo import models, fields, api, exceptions
from odoo.tools.float_utils import float_compare, float_is_zero
from odoo.exceptions import ValidationError


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
    garden_orientation = fields.Selection(string='Type',
                                          selection=[('north', 'North'), ('south', 'South'), ('east', 'East'),
                                                     ('west', 'West')])
    active = fields.Boolean(default=True)
    state = fields.Selection(default='new', required=True, copy=False,
                             selection=[('new', 'New'), ('offer_received', 'Offer Received'),
                                        ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'),
                                        ('canceled', 'Canceled')])
    property_type_id = fields.Many2one('estate.property.type', string='Property type')
    sales_person_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    tag_ids = fields.Many2many('estate.property.tag')
    offer_ids = fields.One2many('estate.property.offer', 'property_id')
    total_area = fields.Integer(compute='_compute_total_era')
    best_price = fields.Float(compute='_compute_best_price')

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)',
         'Price muse be strictly positive'),
        ('check_selling_price', 'CHECK(selling_price >= 0)', 'Property selling price must be positive')
    ]

    @api.depends('living_area', 'garden_area')
    def _compute_total_era(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price')) if len(record.offer_ids) > 0 else 0

    @api.onchange('garden')
    def _onchange_garden_orientation(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'

    @api.constrains('selling_price', 'expected_price')
    def _check_selling_price(self):
        for record in self:
            if float_is_zero(record.selling_price, 2) is False and float_is_zero(record.expected_price, 2) is False:
                if float_compare(record.selling_price, record.expected_price, 0) == -1:
                    raise exceptions.ValidationError('The selling price cannot be lower than 90% of the expected price')

    def action_sold(self):
        for record in self:
            if record.state == 'canceled':
                raise exceptions.UserError('Canceled property cannot be sold')
            record.state = 'sold'
        return True

    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise exceptions.UserError('Sold property cannot be canceled')
            record.state = 'canceled'
        return True

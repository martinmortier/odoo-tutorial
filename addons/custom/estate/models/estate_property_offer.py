from odoo import models, fields, api
from datetime import date, timedelta, time, datetime


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'

    price = fields.Float()
    status = fields.Selection(copy=False, selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)
    validity = fields.Integer(default=7, string='Validity (days)')
    date_deadline = fields.Date(compute='_compute_dead_line', inverse='_inverse_dead_line', string='deadline')

    @api.depends('create_date', 'validity')
    def _compute_dead_line(self):
        for record in self:
            if (record.create_date):
                record.date_deadline = record.create_date + timedelta(days=record.validity)
            else:
                record.date_deadline = date.today() + timedelta(days=record.validity)

    def _inverse_dead_line(self):
        for record in self:
            date_deadline_datetime = datetime.combine(record.date_deadline, time.min)
            record.validity = (date_deadline_datetime - record.create_date).days
            record.validity += 1

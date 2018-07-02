# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class TravelOrder(models.Model):
	_name = 'travel.order'

	partner_id = fields.Many2one('res.partner', default=lambda self: self.env['res.users'].browse(self.env.uid).partner_id)
	schedule_id = fields.Many2one('travel.schedule')

	isPay = fields.Boolean(default=False)

	price_travel = fields.Float('Price',required=True)

	departure = fields.Many2one('travel.pool.line',required=True)
	destination = fields.Many2one('travel.pool.line',required=True)

	departure_date = fields.Date('Departure Date',required=True,related='departure.schedule.departure_date', store=True)
	departure_time = fields.Float('Departure Time',required=True,related='departure.departure_perpool', store=True)

	state = fields.Selection([
            ('order', 'Order'),
            ('waiting', 'Waiting Payment'),
            ('travel', 'Travel Order')
            ],default='order')

	tree_seat_number = fields.One2many('travel.seat.line', 'order_id')
	name = fields.Char(string='Travel Order Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))

	@api.model
	def create(self, vals):

		vals['price_travel'] = sum(seat_line.price for seat_line in self.tree_seat_number)
		
#		for seat_line in self.tree_seat_number:
#			vals['price_travel'] += seat_line.price
	
		if vals.get('name', _('New')) == _('New'):
			vals['name'] = self.env['ir.sequence'].next_by_code('travel.order') or _('New')
			
		return super(TravelOrder, self).create(vals)

	@api.model
	def write(self, vals):
		vals['price_travel'] = sum(seat_line.price for seat_line in self.tree_seat_number)

#		for seat_line in self.tree_seat_number:
#			vals['price_travel'] += seat_line.price

		return super(TravelOrder, self).write(vals)

	def get_cr(self):
		return self._cr

	def confirm(self):
		self.write({'state' : 'waiting'})

	def validate(self):
		self.write({'state' : 'travel'})

	def cancel(self):
		self.write({'state' : 'order'})

#	@api.onchange('departure', 'destination')
#	def _schedule_attr(self):
#		attr = []
#
#		if self.departure is not None:
#			attr.append(('departure', '=', self.departure.pool_location.city_ids.id))
#
#		if self.destination is not None:
#			attr.append(('destination', '=', self.destination.pool_location.city_ids.id))
#
#		if len(attr) > 0:
#			schedule = self.env['travel.schedule'].search(attr)
#
#			if schedule is not None:
#				self.schedule_id = schedule.id
#				self.departure_date = schedule.departure_date
#				self.departure_time = self.departure.departure_perpool
#				return {'domain': {'departure': [('schedule', '=', schedule.id)], 'destination': [('schedule_dest', '=', schedule.id)]}}#, 'value': dict(self)}
#
#			else:
#				return {'warning':{'title':_('Schedule Not Found'), 'message':_('Schedule Not Found that Matches the Given Attribute')}}

	@api.onchange('departure')
	def destination_onchange(self):
#	Pemilihan lokasi tujuan (Destination) berdasarkan keberangkatan (Departure) pada jadwal yang sama
		res = {}
		res['domain'] = {'destination': ['&',('schedule', '=', self.departure.schedule.id),('pool_location', '!=', self.departure.pool_location.id),('pool_location.city_ids','!=',self.departure.pool_location.city_ids.id)]}
		return res

	@api.onchange('destination')
	def destination_onchange(self):
#	Pemilihan lokasi keberangkatan (Departure) berdasarkan tujuan (Destination) pada jadwal yang sama
		res = {}
		res['domain'] = {'departure': ['|',('schedule', '=', self.destination.schedule.id),('pool_location', '!=', self.destination.pool_location.id),('pool_location.city_ids','!=',self.destination.pool_location.city_ids.id)]}
		return res
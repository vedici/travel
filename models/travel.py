# -*- coding: utf-8 -*-
from odoo import models, fields, api

#class TravelProduct(models.Model):
#    _inherit = "product.product"
#
#	departure = fields.Char('Departure',required=True)
#	destination = fields.Char('Destination',required=True)
	
class SeatNumber(models.Model):
	_name = 'travel.order.seat'
#	_sql_constraints = [ 
#        ('travel_order_seat_unique', 
#         'UNIQUE (parent_id, seat_number)', 
#         'Seat have been booked by other customers')] 
	parent_id = fields.Many2one('travel.order')
	seat_number = fields.Integer('seat_number')

class Travel(models.Model):
	_name = 'travel.order'
	
	res_users_id = fields.Many2one('res.users', default=lambda self: self.env.uid)
	partner_id = fields.Many2one('res.partner', default=lambda self: self.env.user.partner_id)
	
	passenger = fields.Char('Name', default = lambda self: self._get_passenger())
	email = fields.Char('Email', default = lambda self: self._get_email())
	phone = fields.Char('Phone Number', default = lambda self: self._get_phone())
	
	departure = fields.Char('Departure',required=True)
	destination = fields.Char('Destination',required=True)

	departure_date = fields.Date('Departure Date',required=True)
	departure_time = fields.Float('Departure Time',required=True)
	state = fields.Selection([
            ('order', 'Order'),
            ('waiting', 'Waiting Payment'),
            ('travel', 'Travel Order'),
            ],default='order')
	vehicle = fields.Char('Vehicle',required=True)
	
#	seat_number = fields.Integer('Seat Number')
	
	tree_seat_number = fields.One2many('travel.order.seat', 'parent_id')
	
	def confirm(self):
		self.write({'state': 'waiting'})
		
		return {
			'warning': {
				'title' : "Do "+str(self.passenger) +" Add New Travel?",
				'message' : str(self.email) + " : " + str(self.phone),
			}
		}
	
	def validate(self):
		self.write({'state': 'travel'})
	
	
	@api.model
	def _get_passenger(self):
	#	pid = self.env.user.partner_id.id;
		if self.partner_id is None:
			self.partner_id = self.env.user.partner_id
	
		name = self.partner_id.name
		#name = self.env['res.partner'].search([('id','=', pid)]).name
		if type(name) is str :
			return name
		else :
			return str(name)

	@api.model
	def _get_email(self):
	#	pid = self.env.user.partner_id.id;
		if self.partner_id is None:
			self.partner_id = self.env.user.partner_id
			
		email = self.partner_id.email
		#email = self.env['res.partner'].search([('id','=', pid)]).email
		
		if type(email) is str :
			return email
		else:
			return str(email)
		
	@api.model
	def _get_phone(self):
	#	pid = self.env.user.partner_id.id;
		if self.partner_id is None:
			self.partner_id = self.env.user.partner_id
			
		phone = self.partner_id.phone
		#phone = self.env['res.partner'].search([('id','=', pid)]).phone
		if type(phone) is str :
			return phone
		else :
			return str(phone)

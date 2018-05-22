# -*- coding: utf-8 -*-
from odoo import models, fields, api

#class TravelProduct(models.Model):
#	_inherit = "product.product"
#
#	departure = fields.Char('Departure',required=True)
#	destination = fields.Char('Destination',required=True)
#	vehicle = fields.Char('Vehicle', required=True)
#	seat_id = fields.One2many('product_id')
	
class SeatNumber(models.Model):
	_name = 'travel.order.seat'
	_sql_constraints = [('travel_order_seat_unique', 'UNIQUE (order_id, seat_number)', 'Seat have been booked')] 
#	product_id = fields.Many2one('product.product')
	order_id = fields.Many2one('travel.order')
	seat_number = fields.Integer()

class Travel(models.Model):
	_name = 'travel.order'
	
	partner_id = fields.Many2one('res.partner', default=lambda self: self.env['res.users'].browse(self.env.uid).partner_id)
	schedule_id = fields.Many2one('travel.schedule')
	
#	passenger = fields.Char('Name', related='partner_id.name')
#	email = fields.Char('Email', related='partner_id.email')
#	phone = fields.Char('Phone Number', related='partner_id.phone')
	
	isPay = fields.Boolean(default=False)
	
	departure = fields.Many2one('pool.place',required=True)
	destination = fields.Many2one('pool.place',required=True)

	departure_date = fields.Date('Departure Date',required=True)
	departure_time = fields.Float('Departure Time',required=True)
	state = fields.Selection([
            ('order', 'Order'),
            ('waiting', 'Waiting Payment'),
            ('travel', 'Travel Order'),
            ],default='order')
	vehicle = fields.Many2one('fleet.vehicle',required=True)
	
	tree_seat_number = fields.One2many('travel.order.seat', 'order_id')

#	@api.depends('partner_id')
#	def _get_user_partner(self):
#		self.partner_id = self.env['res.users'].browse(self.env.uid).partner_id
	
	def confirm(self):
		self.write({'state': 'waiting'})
		
#		return {
#			'warning': {
#				'title' : "Do "+str(self.passenger) +" Add New Travel?",
#				'message' : str(self.email) + " : " + str(self.phone),
#			}
#		}
	
	def validate(self):
		self.write({'state': 'travel'})

#	@api.onchange('departure', 'destination', 'departure_date', 'departure_time')
#	def actionChange(self):
#		pass
		
	
#	@api.model
#	def _get_passenger(self):
#		pid = self.env.user.partner_id.id;
#		if self.partner_id is None:
#			self.partner_id = self.env.user.partner_id
#	
#		name = self.partner_id.name
#		#name = self.env['res.partner'].search([('id','=', pid)]).name
#		if type(name) is str :
#			return name
#		else :
#			return str(name)
#
#	@api.model
#	def _get_email(self):
#		pid = self.env.user.partner_id.id;
#			self.partner_id = self.env.user.partner_id
			
#		email = self.partner_id.email
#		#email = self.env['res.partner'].search([('id','=', pid)]).email
		
#		if type(email) is str :
#			return email
#		else:
#			return str(email)
		
#	@api.model
#	def _get_phone(self):
#		pid = self.env.user.partner_id.id;
#		if self.partner_id is None:
#			self.partner_id = self.env.user.partner_id
			
#		phone = self.partner_id.phone
#		#phone = self.env['res.partner'].search([('id','=', pid)]).phone
#		if type(phone) is str :
#			return phone
#		else :
#			return str(phone)
# -*- coding: utf-8 -*-
from odoo import models, fields, api

class TravelSchedule(models.Model):
	_name = 'travel.schedule'

	departure = fields.Many2one('travel.pool.city', required=True)
	destination = fields.Many2one('travel.pool.city', required=True)
	departure_date = fields.Date('Departure Date',required=True)
	# departure_time = fields.Float('Departure Time',required=True)
	vehicle = fields.Many2one('fleet.vehicle', required=True)
	order_list = fields.One2many('travel.order', 'schedule_id')
	pool_list_dep = fields.One2many('travel.pool.line', 'schedule')
	pool_list_dest = fields.One2many('travel.pool.line', 'schedule')
	price = fields.Float('Price', required=True)

class PoolLine(models.Model):
	_name = 'travel.pool.line'
	schedule = fields.Many2one('travel.schedule', string="Schedule",ondelete='cascade')
	pool_location = fields.Many2one('travel.pool.place')
	name = fields.Char(compute="_compute_pool_name", store=False)
	departure_perpool = fields.Float('Departure Time')

	@api.multi
	def _compute_pool_name(self):
		for record in self:
			record.name = record.pool_location.city_ids.city + '/' + record.pool_location.address

#class Vehicle(models.Model):
#	_inherit = 'fleet.vehicle'

#	schedule_id = fields.Many2one('travel.schedule')

# -*- coding: utf-8 -*-
from odoo import models, fields, api

class TravelSchedule(models.Model):
	_name = 'travel.schedule'
	
	departure = fields.Many2one('travel.pool.city', required=True)
	destination = fields.Many2one('travel.pool.city', required=True)
	departure_date = fields.Date('Departure Date',required=True)
	departure_time = fields.Float('Departure Time',required=True)
	vehicle = fields.Many2one('fleet.vehicle')
	order_list = fields.One2many('travel.order', 'schedule_id')
	pool_list = fields.Many2many('travel.pool.place')
	
#class PoolLine(models.Model):
#	_name = 'pool.line'
#	ref = fields.Many2one('travel.schedule', string="Schedule")
#	pool_location = fields.Many2one('pool.place')
	
#class Vehicle(models.Model):
#	_inherit = 'fleet.vehicle'
	
#	schedule_id = fields.Many2one('travel.schedule')
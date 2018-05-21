# -*- coding: utf-8 -*-
from odoo import models, fields, api

class TravelSchedule(models.Model):
	_name = 'travel.schedule'
	
	departure = fields.Many2one('pool.place', required=True)
	destination = fields.Many2one('pool.place', required=True)
	departure_date = fields.Date('Departure Date',required=True)
	departure_time = fields.Float('Departure Time',required=True)
	vehicle_list = fields.One2many('fleet.vehicle', 'schedule_id')
	
class Vehicle(models.Model):
	_inherit = 'fleet.vehicle'
	
	schedule_id = fields.Many2one('travel.schedule')
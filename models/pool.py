# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PoolCity(models.Model):
	_name = 'travel.pool.city'
	_rec_name = 'city'
	city = fields.Char('City',required=True)
	pools = fields.One2many('travel.pool.place','city_ids')
	
class PoolPlace(models.Model):
	_name = 'travel.pool.place'
	_rec_name = 'address'
	city_ids = fields.Many2one('travel.pool.city')
	address = fields.Text('Address')
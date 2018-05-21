# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PoolPlace(models.Model):
	_name = 'pool.place'
	_rec_name = 'city'
	city = fields.Char('City',required=True)
	address = fields.Char('Address',required=True)
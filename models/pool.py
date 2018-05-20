# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PoolPlace(models.Model):
    _name = 'pool.place'

    city = fields.Char('City',required=True)
    address = fields.Char('Address',required=True)

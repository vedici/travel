#import json
#import array

from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError

#
#	Website Travel untuk Pool
#
class Pool(http.Controller) :
#
# 	Mendapatkan List Pool 
#
#	@http.route('/travel/pools', type='http', auth='public', methods=['GET'], website=True)
	@http.route('/travel/pools', auth='public', website=True)
	def web_pools(self, **kw) :
		listpools = request.env['travel.pool.city'].search([])
		return request.render('travel.pool', {
			'pools' : listpools
		})
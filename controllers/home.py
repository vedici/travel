from odoo import http
from odoo.http import request
#
#	Website Travel untuk Tampilan Order, Pool, dan Schedule
#
class Home(http.Controller) :
#
# 	Mendapatkan Travel Order Berdasarkan User yg Login
#
#	@http.route('/travel/orders', type='http', auth='public', methods=['GET'], website=True)
	@http.route('/travel/orders', auth='public', website=True)
	def web_orders(self, **kw) :

#		uid = request.session.uid
		uid = request.uid

		if uid is not None and isinstance(uid, int):

			partner = request.env['res.users'].browse(uid).partner_id
			travels = request.env['travel.order'].search([('partner_id','=', partner.id)]) #search(['create_uid', '=', uid])

			return request.render('travel.order', {
				'partner' : partner,
				'travels' : travels
			})

		else:
			return request.render('travel.login')

#
# 	Mendapatkan List Pool 
#
#	@http.route('/travel/pools', type='http', auth='public', methods=['GET'], website=True)
	@http.route('/travel/pools', auth='public', website=True)
	def web_pools(self, **kw) :
		listpools = request.env['pool.place'].search([])
		return request.render('travel.pool', {
			'pools' : listpools
		})

#
# 	Mendapatkan List Schedule
#
#	@http.route('/travel/schedules', type='http', auth='public', methods=['GET'], website=True)
	@http.route('/travel/schedules', auth='public', website=True)
	def web_schedules(self, **kw) :

		listschedule = request.env['travel.schedule'].search([])

		return request.render('travel.schedule', {
			'schedules' : listschedule
		})
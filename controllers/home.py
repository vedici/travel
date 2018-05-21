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

		uid = request.session.uid

		if uid is not None:
			partners = request.env['res.partner'].search(['user_id', '=', uid])
#			partner_id = request.env['res.users'].browse(uid).partner_id

			travels = request.env['travel.order'].search(['create_uid', '=', uid]) #search(['partner_id','=', partner_id])

			return request.render('travel.order', {
#				'partners' : partners,
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
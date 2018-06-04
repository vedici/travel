import json
import array

from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError

#
#	Website Travel untuk Proses Order
#
class Order(http.Controller) :
#
# 	Mendapatkan Travel Order Yang Telah Dipesan Berdasarkan User yg Login
#
#	@http.route('/travel/orders', type='http', auth='public', methods=['GET'], website=True)
	@http.route('/travel/orders', auth='public', website=True)
	def web_orders(self, **kw) :

#		uid = request.session.uid
		uid = request.uid

		if uid is not None and isinstance(uid, int):

			partner = request.env['res.users'].browse(uid).partner_id
			travels = request.env['travel.order'].search([('partner_id','=', partner.id)]) #search(['create_uid', '=', uid])
#			base_uri = request.env['ir.config_parameter'].get_param('web.base.url')
			
			return request.render('travel.order', {
				'partner' : partner,
				'travels' : travels
#				'base_uri' : base_uri
			})

		else:
			return request.render('travel.login')

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

#
# 	Mendapatkan Item Schedule
#
#	@http.route('/travel/schedule/<model("travel.schedule"):schedule>/', type='http', auth='public', methods=['GET'], website=True)
	@http.route('/travel/schedule/<model("travel.schedule"):schedule>/', auth='public', website=True)
	def web_schedule_item(self, schedule) :
		
		uid = request.uid

		if uid is not None and isinstance(uid, int):
			
			partner = request.env['res.users'].browse(uid).partner_id
		
			return request.render('travel.schedule-item', {
				'partner' : partner,
				'schedule' : schedule
			})
			
		else:
			return request.render('travel.login')
#
# 	Page Bayar
#
	@http.route('/travel/schedule/<model("travel.schedule"):schedule>/pay', type='http', auth="user", methods=['POST'], website=True)
	def web_pay_order(self, schedule, **kw) :

#		kw['partner_id'] = request.env['res.users'].browse(request.uid).partner_id
		kw['schedule_id'] = schedule.id
		
		seats = kw['seats'].split(',');

#		if not all(isinstance(i, int) for i in [kw['schedule'], kw['departure'], kw['destination']]):
#			return json.dumps(False)
		
#		data['schedule_id'] = kw['schedule']
#		data['departure'] = kw['departure']
#		data['destination'] = kw['destination']

		travel_order = request.env['travel.order']
		_cr = travel_order.get_cr()
		
		try:	
			_cr.autocommit(False)
			
			order = travel_order.create(kw)

			for seat in seats:
				data['seat_number'] = seat
				data['order_id'] = order.id
				request.env['travel.order.seat'].create(data)
				
			_cr.commit()
			
		except ValidationError, e:
			_cr.rollback()
			return json.dumps({'error_fields' : e.args[0]})

		return request.render('travel.order_success')

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


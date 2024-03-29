#import json
#import array
from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError

#
#	Custom Error
#
class SeatBookedError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

#
#	Website Travel untuk Proses Order
#
class Order(http.Controller) :
#
# 	Mendapatkan Travel Order Yang Telah Dipesan Berdasarkan User yg Login
#
#	@http.route('/travel/orders', type='http', auth='public', methods=['GET'], website=True)
	@http.route('/travel/orders', auth='user', website=True)
	def web_orders(self, **kw) :
		uid = request.uid

		partner = request.env['res.users'].browse(uid).partner_id
		travels = request.env['travel.order'].search([('partner_id','=', partner.id)]) #search(['create_uid', '=', uid])

		return request.render('travel.order', {
			'partner' : partner,
			'travels' : travels
		})

#
# 	Page Bayar
#
	@http.route('/travel/schedule/<model("travel.schedule"):schedule>/pay', type='http', auth="user", methods=['POST'], website=True)
	def web_pay_order(self, schedule, **kw) :

		data_order = {}
		data_order['schedule_id'] = schedule.id
		data_order['departure'] = int(kw['departure'])
		data_order['departure_date'] = schedule.departure_date
		data_order['departure_time'] = request.env['travel.pool.line'].browse(data_order['departure']).departure_perpool
		data_order['destination'] = int(kw['destination'])
		data_order['state'] = 'waiting'

		travel_order = request.env['travel.order']
		_cr = travel_order.get_cr()
		
		try:	
			_cr.autocommit(False)

			order = travel_order.create(data_order)
			
			seats = request.httprequest.form.getlist('seats[]')

			for seat in seats:
				data = {'order_id' : order.id, 'seat_list' : seat}
				seat_line = request.env['travel.seat.line']
				
				if seat_line.order_id is None:
					raise SeatBookedError('Seat %s Have Been Booked!' % seat)

				seat_line.create(data)

			travel_order.write(order)

			_cr.commit()

			return request.render('travel.order_success', {
				'title': 'Order Success!',
				'message': 'Please Pay Your Invoice',
				'order': travel_order
			})

		except ValidationError, e:
			_cr.rollback()
			
			return request.render('travel.order_success', {
				'title': 'Order Failed!',
				'message': e
			})
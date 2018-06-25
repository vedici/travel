#import json
#import array

from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError

#
#	Website Travel untuk Schedule
#
class Schedule(http.Controller) :
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
from odoo import http
from odoo.http import request

class Home(http.Controller) :

    @http.route('/travel/home', type='http', auth='public', methods=['GET'], website=True)
    def get_index(self, **kw) :
		
		uid = request.session.uid
		
		if uid is not None:
		
			partners = request.env['res.partner'].search(['user_id', '=', uid])
			
			partner_id = request.env['res.users'].browse(uid).partner_id

			travels = request.env['travel.order'].search(['partner_id','=', partner_id])
			
			return request.render('travel.home', {
				'partners' : partners,
				'travels' : travels,
			})
		
		else:
			return request.render('travel.login')
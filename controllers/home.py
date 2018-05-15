from odoo import http

class Home(http.Controller) :

    @http.route('/travel/home', auth='public', website=True)
    def index(self, **kw) :
        return http.request.render('travel.home', {
            'cities' : ["Bandung", "Jakarta", "Surabaya", "Makassar", "Jayapura"],
        })

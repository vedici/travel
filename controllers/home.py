from odoo import http

class Home(http.Controller) :

    @http.route('/travel/home/', auth='public')
    def index(self, **kw) :
        return 'Hello World'
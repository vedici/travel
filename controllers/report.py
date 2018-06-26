from odoo import http
from odoo.http import request

#
#	Website Travel untuk Report
#
class TravelReport(http.Controller) :
#
# 	Mendownload Report
#
	@http.route('/travel/report/<int:id>', auth='user', website=True)
	def print_order(self, id):
        pdf = request.env['report'].sudo().get_pdf([id], 'travel.report_template', data=None)
        pdfhttpheaders = [('Content-Type', 'application/pdf'), ('Content-Length', len(pdf))]
        return request.make_response(pdf, headers=pdfhttpheaders)
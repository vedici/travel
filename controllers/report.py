from odoo import http
from odoo.http import request

#
#	Website Travel untuk Report
#
class Report(http.Controller) :
#
# 	Mendownload Report
#
	@http.route('/travel/report/<int:id>', auth='user', website=True)
	def print_saleorder(self, id):
        pdf = request.env['report'].sudo().get_pdf([id], 'travel.report_template', data=None)
        pdfhttpheaders = [('Content-Type', 'application/pdf'), ('Content-Length', len(pdf))]
        return request.make_response(pdf, headers=pdfhttpheaders)
{
	'name': 'Travel',
	'description': 'Travel',
	'author': 'Kelompok A1',
	'depends': ['base','website','fleet'],
	'application': True,
	'data': ['views/odoo_page/travel_view.xml',
				'views/odoo_page/travel_menu.xml',
				'views/odoo_page/pool_view.xml',
				'views/odoo_page/schedule_view.xml',
				'views/template/web_template.xml',
				'views/web_page/404.xml',
				'views/web_page/login.xml',
				'views/web_page/order.xml',
				'views/web_page/pool.xml',
				'views/web_page/schedule.xml',
				'security/ir.model.access.csv',
				'security/travel_access_rule.xml',
				'reports/travel_order_report.xml',
				'reports/travel_order_template.xml'],
}

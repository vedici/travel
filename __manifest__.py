{
	'name': 'Travel',
	'description': 'Travel',
	'author': 'Kelompok A1',
	'depends': ['base','website'],
	'application': True,
	'data': ['views/travel_view.xml',
				'views/travel_menu.xml',
				'security/ir.model.access.csv',
				'security/travel_access_rule.xml',
				'views/web_template.xml'],
}
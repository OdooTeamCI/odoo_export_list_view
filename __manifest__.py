# -*- coding: utf-8 -*-
# Copyright 2018 Odoo TEAM CI

{
    'name': 'Odoo export list view',
    'version': '11.0.1.0.0',
    'category': 'Web',
    'author': 'Nougbele Daniel, OdooTeamCI, \
            Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'depends': [
        'web',
    ],
    "data": [
        'views/web_export_view_view.xml',
    ],
    'qweb': [
        "static/src/xml/web_export_view_template.xml",
    ],
    'installable': True,
    'auto_install': False,
    'application': True

}

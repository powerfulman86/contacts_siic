# -*- coding: utf-8 -*-
{
    'name': "Contacts SIIC Customization",
    'summary': """  Contacts SIIC Customization """,
    'description': """ Contacts SIIC Customization  """,
    'author': "SIIC",
    'category': 'Tools',
    'depends': ['base', 'contacts'],
    'data': [
        'views/res_partner.xml',
        'views/partner_category.xml',
    ],
    'images': ['static/description/icon.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}

# -*- coding: utf-8 -*-
# Part of Sananaz Mansuri See LICENSE file for full copyright and licensing details.

{
    'name': 'Scrap Quality Check',
    'version': '1.1.1',
    'category': 'Operations/Inventory',
    'summary': """ Scrap Quality Check""",
    'description': """
                    """,
    'author': "Sananaz Mansuri",
    'website': 'http://www.odoo.com',
    'license': 'Other proprietary',
    'depends': ['stock'],
    'data': [
        'views/stock_scrap.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
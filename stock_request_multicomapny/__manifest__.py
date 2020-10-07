# -*- coding: utf-8 -*-

{
    "name": "Stock Request Multi Company",
    "summary": "Internal request for stock",
    "version": "3.4.0",
    "license": "Other proprietary",
'author': "Sananaz Mansuri",
    'website': 'www.odoo.com',
    "category": "Warehouse Management",
    "depends": [
        "stock",
        "stock_request",
        "purchase",
    ],
    "data": [
        'security/security.xml',
        'views/res_users_view.xml',
        'views/stock_quant_view.xml',
        'views/product_views.xml',
        'wizard/create_po_views.xml',
        'views/stock_request_order_view.xml',
        'views/product_tmpl_views.xml',
    ],
    "installable": True,
}

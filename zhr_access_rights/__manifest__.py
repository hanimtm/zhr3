# -*- coding: utf-8 -*-
{
    'name': 'ZHR Access Rights',
    'category': 'Sales',
    'sequence': 1,
    'version': '15.0.1',
    'license': 'LGPL-3',
    'summary': """ZHR Access Rights""",
    'description': """ZHR Access Rights""",
    'author': 'Aneesh.AV',
    'depends': ['product', 'stock', 'stock'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/menu_view.xml',
        'views/stock_view.xml',
    ],
    'installable': True,
    'application': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

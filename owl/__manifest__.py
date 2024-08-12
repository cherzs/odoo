# -*- coding: utf-8 -*-
{
    'name': 'Owl',
    'version': '17.1.1',
    'summary': """ Owl Summary """,
    'author': 'cherzs',
    'category': 'Technical',
    'depends': ['base', 'web'],
    "data": [
        "views/owl_views.xml",
        "views/templates.xml",
        # "views/rpc_views.xml"
    ],'assets': {
            'web.assets_backend': [
                'owl/static/src/**/*'
            ],
        },
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

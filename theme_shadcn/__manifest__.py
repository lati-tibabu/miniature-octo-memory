# -*- coding: utf-8 -*-
{
    'name': 'Shadcn Theme',
    'description': 'A sleek, modern Odoo theme inspired by shadcn/ui design system',
    'category': 'Theme/Creative',
    'summary': 'Modern theme with clean design, smooth animations, and excellent UX',
    'sequence': 1,
    'version': '18.0.1.0.0',
    'author': 'Your Company',
    'website': 'https://github.com/lati-tibabu/miniature-octo-memory',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'views/assets.xml',
        'views/snippets.xml',
        'views/options.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            'theme_shadcn/static/src/scss/primary_variables.scss',
        ],
        'web.assets_frontend': [
            'theme_shadcn/static/src/scss/theme.scss',
            'theme_shadcn/static/src/js/theme.js',
        ],
    },
    'images': [
        'static/description/cover.png',
        'static/description/theme_screenshot.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': """
        module d'hopital""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Mba Mess",
    'website': "http://www.Mbamess.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '8.0.1.0.0',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'templates.xml',
        'views/patient.xml',
        'data/sequence.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}
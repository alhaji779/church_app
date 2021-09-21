# -*- coding: utf-8 -*-
{
    'name': "church_app",

    'summary': """
        Manage the activities of the presbyterian church""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Mike Kanu",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    # 'images': ['static/description/img_pcn.png'],
    'installable': True,

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml', 
        'views/gen_ass.xml',
        'views/gen_synod.xml',
        'views/gen_pres.xml',
        'views/gen_parish.xml',
        'views/gen_cong.xml',
        'views/mytext.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
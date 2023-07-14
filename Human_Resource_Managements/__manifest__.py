# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Human Resource Management (HRM)',
    'author': 'Phạm Sỹ Quang',
    'version': '1.0',
    'sequence': 3,
    'category': '',
    'summary': '',
    'website': 'https://github.com/JohnsonAudreyRalph?tab=repositories',
    'description': """Phần mềm quản trị nhân viên""",
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'data/sequences.xml',
        'views/menu.xml',
        'views/Employee_Information.xml',
        'views/Department_Information.xml',
        'views/Position_Information.xml',
        'views/Education_Level.xml',
        'views/Salary_Grade.xml',
    ],
    'depends': ['mail'],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False
}

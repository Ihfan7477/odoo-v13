# -*- coding:utf-8 -*-

{
    'name': 'Odoo 13 Payroll',
    'category': 'Generic Modules/Human Resources',
    'version': '13.0.5.0.0',
    'sequence': 1,
    'license': 'LGPL-3',
    'author': 'Odoo Mates, Odoo SA',
    'summary': 'Payroll For Odoo 13 Community Edition',
    'description': "",
    'website': 'http://odoomates.tech',
    'depends': [
        'hr_contract',
        'hr_holidays',
    ],
    'data': [
        'security/hr_payroll_security.xml',
        'security/ir.model.access.csv',
        'data/hr_payroll_sequence.xml',
        'wizard/hr_payroll_payslips_by_employees_views.xml',
        'views/hr_contract_views.xml',
        'views/hr_salary_rule_views.xml',
        'views/hr_payslip_views.xml',
        'views/hr_employee_views.xml',
        'views/hr_payroll_report.xml',
        'data/hr_payroll_data.xml',
        'wizard/hr_payroll_contribution_register_report_views.xml',
        'views/res_config_settings_views.xml',
        'views/report_contribution_register_templates.xml',
        'views/report_payslip_templates.xml',
        'views/report_payslip_details_templates.xml',
    ],
    'images': ['static/description/banner.gif'],
    'application': True,
}

# ats/custom_addons/jobs_module/__manifest__.py

{
    'name': 'Jobs Module',
    'version': '1.0',
    'summary': 'Manage job postings for the ATS',
    'description': 'Custom module to manage job listings in the ATS project',
    'category': 'Human Resources',
    'author': 'Your Name',
    'website': 'https://yourcompany.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/jobs_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

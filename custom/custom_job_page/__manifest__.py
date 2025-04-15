{
    'name': 'Custom Job Page',
    'version': '1.0',
    'summary': 'Job posting and listing module for ATS',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/job_template.xml',
        'data/ata_data.xml',
    ],
    'installable': True,
    'application': True,
}
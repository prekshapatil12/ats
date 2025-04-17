{
    'name': 'Job API',
    'version': '1.0',
    'summary': 'REST API for job listings',
    'description': 'Expose RESTful endpoints to interact with job records from a manually created PostgreSQL table.',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

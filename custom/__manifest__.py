{
    'name': 'Custom Job Page',
    'version': '1.0',
    'summary': 'Displays a custom job listing page on the website',
    'description': 'This module adds a new job listing page at /jobs using the Website and HR modules.',
    'category': 'Website',
    'author': 'The Cloudpros',
    'depends': ['website', 'hr'],
    'data': [
        'views/job_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

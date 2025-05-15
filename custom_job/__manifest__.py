{
    'name': 'Custom Job Portal',
    'version': '1.0.0',
    'category': 'Website',
    'summary': 'Job Listings and Applications for Recruiters and Candidates',
    'description': """
Custom Job Portal
==================
This module allows recruiters to post job vacancies and candidates to view and apply for them through the website.
Features:
- Job listing page
- Job details view
- API endpoint for job data
""",
    'author': 'Preksha Patil',
    'website': 'https://yourcompany.com',
    'license': 'LGPL-3',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/job_template.xml',
        'views/job_form_template.xml',# Add the view file here
    ],
    'assets': {
        'web.assets_frontend': [
            # Include CSS/JS files if needed
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}

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
    'depends': ['base', 'website'],  # Include other modules if needed
    'data': [
        'security/ir.model.access.csv',  # Security rights
        'views/job_postings_views.xml',  # Add views for the job postings
        'views/job_postings_templates.xml',  # Add templates if any
    ],
    'assets': {
        'web.assets_frontend': [
            'custom_job_portal/static/src/css/styles.css',  # Custom CSS
            'custom_job_portal/static/src/js/scripts.js',   # Custom JS
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}

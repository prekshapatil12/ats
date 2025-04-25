from odoo import http
from odoo.http import request

class RestApiDemo(http.Controller):

    @http.route('/api/partners', auth='public', type='json', methods=['GET'], csrf=False)
    def get_partners(self):
        # You can adjust the model search to include the necessary fields if you want to filter or limit results
        partners = request.env['res.partner'].sudo().search([], limit=10)
        return [
            {
                'id': p.id,
                'name': p.name,
                'email': p.email,
                'job_title': p.job_title,
                'company': p.company,
                'work_place': p.work_place,
                'job_location': p.job_location,
                'employment_type': p.employment_type,
                'job_description': p.job_description,
                'skills': p.skills,
            } for p in partners
        ]

    @http.route('/api/partners', auth='public', type='json', methods=['POST'], csrf=False)
    def create_partner(self, **kwargs):
        # Collect job-related fields from request data
        name = kwargs.get('name')
        email = kwargs.get('email')
        job_title = kwargs.get('job_title')
        company = kwargs.get('company')
        work_place = kwargs.get('work_place')
        job_location = kwargs.get('job_location')
        employment_type = kwargs.get('employment_type')
        job_description = kwargs.get('job_description')
        skills = kwargs.get('skills')

        if not name:
            return {'error': 'Name is required'}

        # Create the partner with the additional job-related fields
        partner = request.env['res.partner'].sudo().create({
            'name': name,
            'email': email,
            'job_title': job_title,
            'company': company,
            'work_place': work_place,
            'job_location': job_location,
            'employment_type': employment_type,
            'job_description': job_description,
            'skills': skills,
        })

        # Return the created partner details, including the job-related fields
        return {
            'id': partner.id,
            'name': partner.name,
            'email': partner.email,
            'job_title': partner.job_title,
            'company': partner.company,
            'work_place': partner.work_place,
            'job_location': partner.job_location,
            'employment_type': partner.employment_type,
            'job_description': partner.job_description,
            'skills': partner.skills,
        }

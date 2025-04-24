from odoo import http
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)

class RestApiDemo(http.Controller):

    @http.route('/api/partners', auth='public', type='json', methods=['GET'], csrf=False)
    def get_partners(self):
        partners = request.env['res.partner'].sudo().search([], limit=10)
        return [
            {
                'id': p.id,
                'name': p.name,
                'email': p.email
            } for p in partners
        ]

    @http.route('/api/partners', auth='public', type='json', methods=['POST'], csrf=False)
    def create_partner(self, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        if not name:
            return {'error': 'Name is required'}
        partner = request.env['res.partner'].sudo().create({
            'name': name,
            'email': email
        })
        return {
            'id': partner.id,
            'name': partner.name,
            'email': partner.email
        }


class JobWebsite(http.Controller):

    @http.route('/jobs', type='http', auth='public', website=True)
    def list_jobs(self, **kwargs):
        jobs = request.env['custom.job'].sudo().search([('is_published', '=', True)])
        _logger.info(f"Loaded {len(jobs)} jobs for display on /jobs page.")
        return request.render('custom_job.job_listing_template', {
            'jobs': jobs
        })

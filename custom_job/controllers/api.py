from odoo import http
from odoo.http import request

class JobWebsite(http.Controller):

    @http.route('/jobs', type='http', auth='public', website=True)
    def list_jobs(self, **kwargs):
        jobs = request.env['custom.job'].sudo().search([('is_published', '=', True)])
        return request.render('custom_job.job_listing_template', {
            'jobs': jobs
        })

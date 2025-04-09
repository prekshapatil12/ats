from odoo import http
from odoo.http import request

class JobPage(http.Controller):

    @http.route(['/jobs'], type='http', auth='public', website=True)
    def job_list(self):
        jobs = request.env['hr.job'].sudo().search([])
        return request.render('custom_job_page.custom_job_page', {
            'jobs': jobs
        })

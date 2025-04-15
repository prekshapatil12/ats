from odoo import http
from odoo.http import request

class JobController(http.Controller):

    @http.route('/jobs', type='http', auth='public', website=True)
    def list_jobs(self, **kwargs):
        jobs = request.env['custom.job'].sudo().search([])
        html = "<h1>Job Listings</h1><ul>"
        for job in jobs:
            html += f"<li><strong>{job.name}</strong> - {job.department}</li>"
        html += "</ul>"
        return html

    @http.route('/jobs/<int:job_id>', type='http', auth='public', website=True)
    def job_detail(self, job_id, **kwargs):
        job = request.env['custom.job'].sudo().browse(job_id)
        if not job.exists():
            return "<h2>Job not found</h2>"
        return f"""
            <h1>{job.name}</h1>
            <p><strong>Department:</strong> {job.department}</p>
            <p><strong>Description:</strong> {job.description}</p>
            <p><strong>Status:</strong> {"Active" if job.is_active else "Inactive"}</p>
        """
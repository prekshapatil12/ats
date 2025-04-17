from odoo import http
from odoo.http import request
from datetime import datetime

class JobAPI(http.Controller):

    @http.route('/api/jobs', type='json', auth='public', methods=['GET'], csrf=False)
    def get_jobs(self):
        jobs = request.env['custom.job'].sudo().search_read([], [])
        return {'status': 200, 'data': jobs}

    @http.route('/api/jobs/<int:job_id>', type='json', auth='public', methods=['GET'], csrf=False)
    def get_job(self, job_id):
        job = request.env['custom.job'].sudo().browse(job_id)
        if job.exists():
            return {'status': 200, 'data': job.read()[0]}
        return {'status': 404, 'message': 'Job not found'}

    @http.route('/api/jobs', type='json', auth='public', methods=['POST'], csrf=False)
    def create_job(self, **post):
        post['created_at'] = datetime.now()
        post['updated_at'] = datetime.now()
        job = request.env['custom.job'].sudo().create(post)
        return {'status': 201, 'id': job.id}

    @http.route('/api/jobs/<int:job_id>', type='json', auth='public', methods=['PUT'], csrf=False)
    def update_job(self, job_id, **post):
        job = request.env['custom.job'].sudo().browse(job_id)
        if not job.exists():
            return {'status': 404, 'message': 'Job not found'}
        post['updated_at'] = datetime.now()
        job.write(post)
        return {'status': 200, 'message': 'Job updated'}

    @http.route('/api/jobs/<int:job_id>', type='json', auth='public', methods=['PATCH'], csrf=False)
    def patch_job(self, job_id, **patch_data):
        job = request.env['custom.job'].sudo().browse(job_id)
        if not job.exists():
            return {'status': 404, 'message': 'Job not found'}
        patch_data['updated_at'] = datetime.now()
        job.write(patch_data)
        return {'status': 200, 'message': 'Job partially updated'}

    @http.route('/api/jobs/<int:job_id>', type='json', auth='public', methods=['DELETE'], csrf=False)
    def delete_job(self, job_id):
        job = request.env['custom.job'].sudo().browse(job_id)
        if not job.exists():
            return {'status': 404, 'message': 'Job not found'}
        job.unlink()
        return {'status': 200, 'message': 'Job deleted'}

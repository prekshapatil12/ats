# from odoo import http
# from odoo.http import request, Response
# import json
# class JobAPIController(http.Controller):
#     @http.route('/api/jobs', type='http', auth='public', methods=['GET'], csrf=False)
#     def get_jobs(self, **kwargs):
#         try:
#             jobs = request.env['job.postings'].sudo().search([])
#             job_list = []
#             for job in jobs:
#                 job_list.append({
#                     'job_id': job.job_id,
#                     'job_title': job.job_title,
#                     'experience': job.experience,
#                     'responsibilities': job.responsibilities,
#                     'requirement': job.requirement,
#                     'skills': job.skills,
#                     'status': job.status,
#                     'workplace_type': job.workplace_type,
#                     'shift': job.shift,
#                     'company': job.company,
#                     'location': job.location,
#                     'salary': job.salary,
#                     'posted_date': str(job.posted_date),
#                     'joining_tentative_date': str(job.joining_tentative_date),
#                 })
#             return Response(
#                 json.dumps({'status': 200, 'data': job_list}),
#                 content_type='application/json',
#                 status=200
#             )
#         except Exception as e:
#             return Response(
#                 json.dumps({'status': 500, 'error': str(e)}),
#                 content_type='application/json', 
#                 status=500
#             )

from odoo import http
from odoo.http import request, Response
import json

class JobAPIController(http.Controller):
    @http.route('/api/jobs', type='json', auth='public', methods=['GET'], csrf=False)
    def get_jobs(self, **kwargs):
        try:
            jobs = request.env['job.postings'].sudo().search([])
            job_list = [{
                'job_id': job.job_id,
                'job_title': job.job_title,
                'experience': job.experience,
                'responsibilities': job.responsibilities,
                'requirement': job.requirement,
                'skills': job.skills,
                'status': job.status,
                'workplace_type': job.workplace_type,
                'shift': job.shift,
                'company': job.company,
                'location': job.location,
                'salary': job.salary,
                'posted_date': str(job.posted_date),
                'joining_tentative_date': str(job.joining_tentative_date),
            } for job in jobs]
            return {'status': 200, 'data': job_list}
        except Exception as e:
            return {'status': 500, 'error': str(e)}

    @http.route('/api/jobs', type='json', auth='public', methods=['POST'], csrf=False)
    def create_job(self, **kwargs):
        try:
            job = request.env['job.postings'].sudo().create(kwargs)
            return {'status': 201, 'message': 'Job created', 'job_id': job.id}
        except Exception as e:
            return {'status': 500, 'error': str(e)}

    @http.route('/api/jobs/<int:job_id>', type='json', auth='public', methods=['PUT'], csrf=False)
    def update_job_put(self, job_id, **kwargs):
        try:
            job = request.env['job.postings'].sudo().browse(job_id)
            if not job.exists():
                return {'status': 404, 'message': 'Job not found'}
            job.write(kwargs)  # Overwrites fields
            return {'status': 200, 'message': 'Job updated'}
        except Exception as e:
            return {'status': 500, 'error': str(e)}

    @http.route('/api/jobs/<int:job_id>', type='json', auth='public', methods=['PATCH'], csrf=False)
    def update_job_patch(self, job_id, **kwargs):
        try:
            job = request.env['job.postings'].sudo().browse(job_id)
            if not job.exists():
                return {'status': 404, 'message': 'Job not found'}
            job.write(kwargs)  # Partially updates fields
            return {'status': 200, 'message': 'Job partially updated'}
        except Exception as e:
            return {'status': 500, 'error': str(e)}

    @http.route('/api/jobs/<int:job_id>', type='json', auth='public', methods=['DELETE'], csrf=False)
    def delete_job(self, job_id, **kwargs):
        try:
            job = request.env['job.postings'].sudo().browse(job_id)
            if not job.exists():
                return {'status': 404, 'message': 'Job not found'}
            job.unlink()
            return {'status': 200, 'message': 'Job deleted'}
        except Exception as e:
            return {'status': 500, 'error': str(e)}

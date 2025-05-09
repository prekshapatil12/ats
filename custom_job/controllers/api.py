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
from odoo.http import request
from datetime import datetime
import json

class JobAPIController(http.Controller):

    @http.route('/api/jobs', type='json', auth='public', methods=['GET'], csrf=False)
    def get_jobs(self, **kwargs):
        try:
            jobs = request.env['job.postings'].sudo().search([])
            job_list = [{
                'job_id': job.id,
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
                'posted_date': job.posted_date.strftime('%Y-%m-%d') if job.posted_date else None,
                'joining_tentative_date': job.joining_tentative_date.strftime('%Y-%m-%d') if job.joining_tentative_date else None,
            } for job in jobs]
            return {'status': 200, 'data': job_list}
        except Exception as e:
            return {'status': 500, 'error': str(e)}

    @http.route('/api/jobs', type='json', auth='public', methods=['POST'], csrf=False)
    def create_job(self, **kwargs):
        try:
            data = kwargs  # Since type='json', kwargs contains the parsed JSON data

            required_fields = [
                'job_id','job_title', 'experience', 'skills', 'status',
                'company', 'location', 'posted_date', 'joining_tentative_date'
            ]
            missing_fields = [field for field in required_fields if not data.get(field)]
            if missing_fields:
                return {'status': 400, 'error': f'Missing required fields: {", ".join(missing_fields)}'}

            posted_date = datetime.strptime(data.get('posted_date'), '%Y-%m-%d').date()
            joining_tentative_date = datetime.strptime(data.get('joining_tentative_date'), '%Y-%m-%d').date()

            job = request.env['job.postings'].sudo().create({
                'job_id': data.get('job_id'),
                'job_title': data.get('job_title'),
                'experience': data.get('experience'),
                'skills': data.get('skills'),
                'status': data.get('status'),
                'workplace_type': data.get('workplace_type'),
                'shift': data.get('shift'),
                'company': data.get('company'),
                'location': data.get('location'),
                'posted_date': posted_date,
                'joining_tentative_date': joining_tentative_date,
                'responsibilities': data.get('responsibilities'),
                'requirement': data.get('requirement'),
                'salary': data.get('salary'),
            })

            return {'status': 201, 'message': 'Job created successfully', 'job_id': job.id}

        except Exception as e:
            return {'status': 500, 'error': str(e)}

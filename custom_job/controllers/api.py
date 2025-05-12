from odoo import http
from odoo.http import request, Response
import json
class JobAPIController(http.Controller):
    @http.route('/api/jobs', type='http', auth='public', methods=['GET'], csrf=False)
    def get_jobs(self, **kwargs):
        try:
            jobs = request.env['job.postings'].sudo().search([])
            job_list = []
            for job in jobs:
                job_list.append({
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
                })
            return Response(
                json.dumps({'status': 200, 'data': job_list}),
                content_type='application/json',
                status=200
            )
        except Exception as e:
            return Response(
                json.dumps({'status': 500, 'error': str(e)}),
                content_type='application/json', 
                status=500
            )

    @http.route('/api/jobs', type='json', auth='public', methods=['POST'], csrf=False)
    def create_job(self, **kwargs):
        try:
            # Read JSON data from request
            data = request.jsonrequest

            # Validate required fields (add more as needed)
            required_fields = ['job_id', 'job_title', 'experience', 'responsibilities', 
                               'requirement', 'skills', 'status', 'workplace_type', 
                               'shift', 'company', 'location', 'salary', 
                               'posted_date', 'joining_tentative_date']
            for field in required_fields:
                if field not in data:
                    return Response(
                        json.dumps({'status': 400, 'error': f'Missing required field: {field}'}),
                        content_type='application/json',
                        status=400
                    )

            # Create the job record
            job = request.env['job.postings'].sudo().create({
                'job_id': data['job_id'],
                'job_title': data['job_title'],
                'experience': data['experience'],
                'responsibilities': data['responsibilities'],
                'requirement': data['requirement'],
                'skills': data['skills'],
                'status': data['status'],
                'workplace_type': data['workplace_type'],
                'shift': data['shift'],
                'company': data['company'],
                'location': data['location'],
                'salary': data['salary'],
                'posted_date': data['posted_date'],
                'joining_tentative_date': data['joining_tentative_date'],
            })

            return Response(
                json.dumps({'status': 201, 'message': 'Job created successfully', 'job_id': job.id}),
                content_type='application/json',
                status=201
            )
        except Exception as e:
            return Response(
                json.dumps({'status': 500, 'error': str(e)}),
                content_type='application/json',
                status=500
            )
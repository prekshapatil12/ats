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
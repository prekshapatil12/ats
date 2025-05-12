from odoo import http
from odoo.http import request
import json



class JobAPIController(http.Controller):

    @http.route('/api/jobs', type='json', auth='public', methods=['GET'], csrf=False)
    def get_all_jobs(self):
        # Fetch all job postings from the job.postings model
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
        return {'status': 200, 'jobs': job_list}

@http.route('/api/jobs', type='json', auth='public', methods=['POST'], csrf=False)
    def create_job_posting(self):
        try:
            data = request.jsonrequest  # Get the JSON body
            new_job = request.env['job.postings'].sudo().create({
                'job_id': data.get('job_id'),
                'job_title': data.get('job_title'),
                'experience': data.get('experience'),
                'responsibilities': data.get('responsibilities'),
                'requirement': data.get('requirement'),
                'skills': data.get('skills'),
                'status': data.get('status'),
                'workplace_type': data.get('workplace_type'),
                'shift': data.get('shift'),
                'company': data.get('company'),
                'location': data.get('location'),
                'salary': data.get('salary'),
                'posted_date': data.get('posted_date'),
                'joining_tentative_date': data.get('joining_tentative_date'),
            })
            return {
                'status': 201,
                'message': 'Job created successfully',
                'job_id': new_job.id
            }
        except Exception as e:
            return {
                'status': 500,
                'error': str(e)
            }







      
    
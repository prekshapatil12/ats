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
    def create_job_posting(self, **kwargs):
        try:
            # Extract the data from the incoming JSON payload
            job_data = {
                'job_id': kwargs.get('job_id'),
                'job_title': kwargs.get('job_title'),
                'experience': kwargs.get('experience'),
                'responsibilities': kwargs.get('responsibilities'),
                'requirement': kwargs.get('requirement'),
                'skills': kwargs.get('skills'),
                'status': kwargs.get('status'),
                'workplace_type': kwargs.get('workplace_type'),
                'shift': kwargs.get('shift'),
                'company': kwargs.get('company'),
                'location': kwargs.get('location'),
                'salary': kwargs.get('salary'),
                'posted_date': kwargs.get('posted_date'),
                'joining_tentative_date': kwargs.get('joining_tentative_date'),
            }

            # Create a new job posting record in the job.postings model
            new_job = request.env['job.postings'].sudo().create(job_data)

            # Return a success response with the newly created job's ID
            return {
                'status': 201,
                'message': 'Job created successfully',
                'job_id': new_job.id
            }

        except Exception as e:
            # Return error details if something goes wrong
             _logger.error("Error in job creation: %s", str(e))  # Add this
             return Response(
             json.dumps({'status': 500, 'error': str(e)}),
             content_type='application/json',
             status=500
        )
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
      def create_job(self, **kwargs):
        try:
            # Extract fields from JSON body
            job_data = request.jsonrequest

            # Validate required fields (example: job_title and company)
            required_fields = ['job_id', 'job_title', 'experience', 'responsibilities',
                               'requirement', 'skills', 'status', 'workplace_type',
                               'shift', 'company', 'location', 'salary',
                               'posted_date', 'joining_tentative_date']
            for field in required_fields:
                if field not in job_data:
                    return {'status': 400, 'error': f'Missing required field: {field}'}

            # Create the job posting record
            job = request.env['job.postings'].sudo().create({
                'job_id': job_data['job_id'],
                'job_title': job_data['job_title'],
                'experience': job_data['experience'],
                'responsibilities': job_data['responsibilities'],
                'requirement': job_data['requirement'],
                'skills': job_data['skills'],
                'status': job_data['status'],
                'workplace_type': job_data['workplace_type'],
                'shift': job_data['shift'],
                'company': job_data['company'],
                'location': job_data['location'],
                'salary': job_data['salary'],
                'posted_date': job_data['posted_date'],
                'joining_tentative_date': job_data['joining_tentative_date'],
            })

            return {'status': 201, 'message': 'Job created successfully', 'job_id': job.id}
        
        except Exception as e:
            return {'status': 500, 'error': str(e)}

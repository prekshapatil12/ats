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
        """
        Create a new job posting (expects raw JSON).
        """
        try:
            # Safely parse raw JSON from the body
            job_data = json.loads(request.httprequest.data.decode('utf-8'))

            required_fields = [
                'job_id', 'job_title', 'experience', 'responsibilities',
                'requirement', 'skills', 'status', 'workplace_type',
                'shift', 'company', 'location', 'salary',
                'posted_date', 'joining_tentative_date'
            ]

            # Validate required fields
            missing_fields = [field for field in required_fields if field not in job_data]
            if missing_fields:
                return {
                    'status': 400,
                    'error': f"Missing required fields: {', '.join(missing_fields)}"
                }

            # Create the job posting
            job = request.env['job.postings'].sudo().create({
                key: job_data[key] for key in required_fields
            })

            return {
                'status': 201,
                'message': 'Job created successfully',
                'job_id': job.id
            }

        except Exception as e:
            return {
                'status': 500,
                'error': f"Internal Server Error: {str(e)}"
            }
          
     @http.route('/api/jobs/<string:job_id>', type='json', auth='public', methods=['PUT'], csrf=False)
     def update_job(self, job_id, **kwargs):
        """
        Update an existing job posting by its database ID.
        Expects raw JSON body with fields to update.
        """
        try:
            job_data = json.loads(request.httprequest.data.decode('utf-8'))

            # Find the job by ID
            job = request.env['job.postings'].sudo().browse(job_id)
            if not job.exists():
                return {
                    'status': 404,
                    'error': f'Job with ID {job_id} not found'
                }

            # Only update the fields that are present in the payload
            updatable_fields = [
                'job_id', 'job_title', 'experience', 'responsibilities',
                'requirement', 'skills', 'status', 'workplace_type',
                'shift', 'company', 'location', 'salary',
                'posted_date', 'joining_tentative_date'
            ]

            update_values = {key: job_data[key] for key in updatable_fields if key in job_data}

            if not update_values:
                return {
                    'status': 400,
                    'error': 'No valid fields provided for update'
                }

            job.write(update_values)

            return {
                'status': 200,
                'message': f'Job with ID {job_id} updated successfully'
            }

        except Exception as e:
            return {
                'status': 500,
                'error': f'Internal Server Error: {str(e)}'
            }      
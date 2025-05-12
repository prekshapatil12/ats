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
            data = request.jsonrequest
            required_fields = [
                'job_id', 'job_title', 'experience', 'responsibilities',
                'requirement', 'skills', 'company', 'location', 'salary',
                'posted_date', 'joining_tentative_date'
            ]

            # Validate required fields
            missing_fields = [f for f in required_fields if not data.get(f)]
            if missing_fields:
                return {
                    'status': 400,
                    'error': f"Missing required fields: {', '.join(missing_fields)}"
                }

            # Validate date fields
            for field in ['posted_date', 'joining_tentative_date']:
                try:
                    datetime.strptime(data.get(field), "%Y-%m-%d")
                except ValueError:
                    return {
                        'status': 400,
                        'error': f"Invalid date format for {field}. Expected YYYY-MM-DD."
                    }

            # Create job posting
            job = request.env['job.postings'].sudo().create({
                'job_id': data.get('job_id'),
                'job_title': data.get('job_title'),
                'experience': data.get('experience'),
                'responsibilities': data.get('responsibilities'),
                'requirement': data.get('requirement'),
                'skills': data.get('skills'),
                'status': data.get('status', 'open'),
                'workplace_type': data.get('workplace_type', 'hybrid'),
                'shift': data.get('shift', 'day'),
                'company': data.get('company'),
                'location': data.get('location'),
                'salary': data.get('salary'),
                'posted_date': data.get('posted_date'),
                'joining_tentative_date': data.get('joining_tentative_date'),
            })

            return {
                'status': 201,
                'message': 'Job created successfully',
                'job': {
                    'id': job.id,
                    'job_id': job.job_id,
                    'title': job.job_title
                }
            }

        except Exception as e:
            _logger.exception("Job creation failed")
            return {
                'status': 500,
                'error': 'Internal Server Error. Check server logs.'
            }
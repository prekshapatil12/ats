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
    
    
     @http.route('/api/jobs', auth='public', type='json', methods=['POST'], csrf=False)
     def create_job_posting(self, **kwargs):
        required_fields = [
            'job_id', 'job_title', 'experience', 'responsibilities', 'requirement',
            'skills', 'company', 'location', 'salary',
            'posted_date', 'joining_tentative_date',
            'create_uid', 'create_date', 'write_uid', 'write_date'
        ]
        missing_fields = [field for field in required_fields if not kwargs.get(field)]

        if missing_fields:
            return {
                'success': False,
                'error': f"Missing required fields: {', '.join(missing_fields)}"
            }

        try:
            # Validate date fields
            for date_field in ['posted_date', 'joining_tentative_date', 'create_date', 'write_date']:
                try:
                    datetime.strptime(kwargs[date_field], "%Y-%m-%d")
                except ValueError:
                    return {
                        'success': False,
                        'error': f"Invalid date format for '{date_field}', expected 'YYYY-MM-DD'"
                    }

            values = {
                'job_id': kwargs.get('job_id'),
                'job_title': kwargs.get('job_title'),
                'experience': kwargs.get('experience'),
                'responsibilities': kwargs.get('responsibilities'),
                'requirement': kwargs.get('requirement'),
                'skills': kwargs.get('skills'),
                'status': kwargs.get('status', 'open'),
                'workplace_type': kwargs.get('workplace_type', 'hybrid'),
                'shift': kwargs.get('shift', 'day'),
                'company': kwargs.get('company'),
                'location': kwargs.get('location'),
                'salary': kwargs.get('salary'),
                'posted_date': kwargs.get('posted_date'),
                'joining_tentative_date': kwargs.get('joining_tentative_date'),
                'create_uid': int(kwargs.get('create_uid')),
                'create_date': kwargs.get('create_date'),
                'write_uid': int(kwargs.get('write_uid')),
                'write_date': kwargs.get('write_date'),
            }

            job_posting = request.env['job.postings'].sudo().create(values)

            return {
                'success': True,
                'message': 'Job created successfully',
                'job': {
                    'id': job_posting.id,
                    'job_id': job_posting.job_id,
                    'job_title': job_posting.job_title,
                    'status': job_posting.status
                }
            }

        except Exception as e:
            _logger.error(f"Error creating job posting: {str(e)}", exc_info=True)
            return {
                'success': False,
                'error': 'Internal Server Error. Check logs for details.'
            }
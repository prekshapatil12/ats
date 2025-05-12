from odoo import http
from odoo.http import request
from datetime import datetime
import json
import logging

_logger = logging.getLogger(__name__)

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
    
    
    # @http.route('/api/jobs', type='json', auth='public', methods=['POST'], csrf=False)
    # def create_job_posting(self, **kwargs):
    #     try:
    #         # Extract the data from the incoming JSON payload
    #         job_data = {
    #             'job_id': kwargs.get('job_id'),
    #             'job_title': kwargs.get('job_title'),
    #             'experience': kwargs.get('experience'),
    #             'responsibilities': kwargs.get('responsibilities'),
    #             'requirement': kwargs.get('requirement'),
    #             'skills': kwargs.get('skills'),
    #             'status': kwargs.get('status'),
    #             'workplace_type': kwargs.get('workplace_type'),
    #             'shift': kwargs.get('shift'),
    #             'company': kwargs.get('company'),
    #             'location': kwargs.get('location'),
    #             'salary': kwargs.get('salary'),
    #             'posted_date': kwargs.get('posted_date'),
    #             'joining_tentative_date': kwargs.get('joining_tentative_date'),
    #         }

    #         # Create a new job posting record in the job.postings model
    #         new_job = request.env['job.postings'].sudo().create(job_data)

    #         # Return a success response with the newly created job's ID
    #         return {
    #             'status': 201,
    #             'message': 'Job created successfully',
    #             'job_id': new_job.id
    #         }

    #     except Exception as e:
    #         # Return error details if something goes wrong
    #         return {'status': 500, 'error': str(e)}
    
       @http.route('/api/jobs', auth='public', type='json', methods=['POST'], csrf=False)
       def create_job_posting(self, **kwargs):
        required_fields = [
            'job_id', 'job_title', 'experience', 'responsibilities', 'requirement',
            'skills', 'company', 'location', 'salary', 'posted_date', 'joining_tentative_date'
        ]
        missing_fields = [field for field in required_fields if not kwargs.get(field)]

        if missing_fields:
            return {
                'success': False,
                'error': f"Missing required field(s): {', '.join(missing_fields)}"
            }

        try:
            # Optional: convert dates if fields are Date or Datetime
            for date_field in ['posted_date', 'joining_tentative_date']:
                if kwargs.get(date_field):
                    try:
                        # adjust format as per your field type (Date or Datetime)
                        datetime.strptime(kwargs[date_field], "%Y-%m-%d")
                    except ValueError:
                        return {
                            'success': False,
                            'error': f"Invalid date format for '{date_field}', expected 'YYYY-MM-DD'"
                        }

            values = {
                field: kwargs.get(field) for field in required_fields
            }

            # Set optional fields with defaults
            values.update({
                'status': kwargs.get('status', 'open'),
                'workplace_type': kwargs.get('workplace_type', 'hybrid'),
                'shift': kwargs.get('shift', 'day')
            })

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
                'error': 'Internal Server Error. Check logs for more info.'
            }
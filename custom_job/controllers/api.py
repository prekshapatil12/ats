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
        Update an existing job posting using the custom job_id.
        """
        try:
            # Parse the raw JSON body
            job_data = json.loads(request.httprequest.data.decode('utf-8'))

            if not job_data:
                return {'status': 400, 'error': 'No data provided in the request body.'}

            # Search for the job by custom job_id
            job = request.env['job.postings'].sudo().search([('job_id', '=', job_id)], limit=1)
            if not job:
                return {'status': 404, 'error': f"No job found with job_id '{job_id}'"}

            # Fields allowed to be updated (from your model)
            allowed_fields = [
                'job_title', 'experience', 'responsibilities',
                'requirement', 'skills', 'status', 'workplace_type',
                'shift', 'company', 'location', 'salary',
                'posted_date', 'joining_tentative_date'
            ]

            # Prepare values to update
            update_values = {field: job_data[field] for field in allowed_fields if field in job_data}

            if not update_values:
                return {'status': 400, 'error': 'No valid fields provided for update.'}

            # Write updates to the job record
            job.write(update_values)

            return {
                'status': 200,
                'message': f"Job with job_id '{job_id}' updated successfully.",
                'updated_fields': list(update_values.keys())
            }

        except Exception as e:
            
            return {'status': 500, 'error': f"Internal Server Error: {str(e)}"}
        """
        Update an existing job posting using the custom job_id field.
        Expects a JSON body with fields to update.
        """
        try:
            # Parse JSON request body
            job_data = request.jsonrequest

            if not job_data:
                return {'status': 400, 'error': 'No data provided in the request body.'}

            # Search for the job using job_id
            job = request.env['job.postings'].sudo().search([('job_id', '=', job_id)], limit=1)
            if not job:
                return {'status': 404, 'error': f"No job found with job_id '{job_id}'"}

            # Define updatable fields from your model
            updatable_fields = [
                'job_title', 'experience', 'responsibilities',
                'requirement', 'skills', 'status', 'workplace_type',
                'shift', 'company', 'location', 'salary',
                'posted_date', 'joining_tentative_date'
            ]

            # Build the dictionary with only valid fields present in request
            update_values = {field: job_data[field] for field in updatable_fields if field in job_data}

            if not update_values:
                return {'status': 400, 'error': 'No valid fields provided to update.'}

            # Write (update) the job
            job.write(update_values)

            return {
                'status': 200,
                'message': f"Job with job_id '{job_id}' updated successfully.",
                'updated_fields': list(update_values.keys())
            }

        except Exception as e:
            
            return {'status': 500, 'error': f"Internal Server Error: {str(e)}"}
        """
        Create a new job posting (expects raw JSON).
        """
        try:
            # Safely parse raw JSON from the body
            job_data = json.loads(request.httprequest.data.decode('utf-8'))

            job = request.env['job.postings'].sudo().browse(job_id)
            if not job.exists():
                return {
                    'status': 404,
                    'error': f'Job with ID {job_id} not found'
                }

            
            updatable_fields = [
                'job_title', 'experience', 'responsibilities',
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
                'status': 201,
                'message': 'Job Updated successfully',
                'job_id': job.id
            }

        except Exception as e:
            return {
                'status': 500,
                'error': f"Internal Server Error: {str(e)}"
            }
            

     
    @http.route('/api/jobs/<string:job_id>', type='json', auth='public', methods=['PATCH'], csrf=False)
    def update_job(self, job_id, **kwargs):
        """
        Update an existing job posting using the custom job_id.
        """
        try:
            # Parse the raw JSON body
            job_data = json.loads(request.httprequest.data.decode('utf-8'))

            if not job_data:
                return {'status': 400, 'error': 'No data provided in the request body.'}

            # Search for the job by custom job_id
            job = request.env['job.postings'].sudo().search([('job_id', '=', job_id)], limit=1)
            if not job:
                return {'status': 404, 'error': f"No job found with job_id '{job_id}'"}

            # Fields allowed to be updated (from your model)
            allowed_fields = [
                'job_title', 'experience', 'responsibilities',
                'requirement', 'skills', 'status', 'workplace_type',
                'shift', 'company', 'location', 'salary',
                'posted_date', 'joining_tentative_date'
            ]

            # Prepare values to update
            update_values = {field: job_data[field] for field in allowed_fields if field in job_data}

            if not update_values:
                return {'status': 400, 'error': 'No valid fields provided for update.'}

            # Write updates to the job record
            job.write(update_values)

            return {
                'status': 200,
                'message': f"Job with job_id '{job_id}' updated successfully.",
                'updated_fields': list(update_values.keys())
            }

        except Exception as e:
            
            return {'status': 500, 'error': f"Internal Server Error: {str(e)}"}
        """
        Update an existing job posting using the custom job_id field.
        Expects a JSON body with fields to update.
        """
        try:
            # Parse JSON request body
            job_data = request.jsonrequest

            if not job_data:
                return {'status': 400, 'error': 'No data provided in the request body.'}

            # Search for the job using job_id
            job = request.env['job.postings'].sudo().search([('job_id', '=', job_id)], limit=1)
            if not job:
                return {'status': 404, 'error': f"No job found with job_id '{job_id}'"}

            # Define updatable fields from your model
            updatable_fields = [
                'job_title', 'experience', 'responsibilities',
                'requirement', 'skills', 'status', 'workplace_type',
                'shift', 'company', 'location', 'salary',
                'posted_date', 'joining_tentative_date'
            ]

            # Build the dictionary with only valid fields present in request
            update_values = {field: job_data[field] for field in updatable_fields if field in job_data}

            if not update_values:
                return {'status': 400, 'error': 'No valid fields provided to update.'}

            # Write (update) the job
            job.write(update_values)

            return {
                'status': 200,
                'message': f"Job with job_id '{job_id}' updated successfully.",
                'updated_fields': list(update_values.keys())
            }

        except Exception as e:
            
            return {'status': 500, 'error': f"Internal Server Error: {str(e)}"}
        """
        Create a new job posting (expects raw JSON).
        """
        try:
            # Safely parse raw JSON from the body
            job_data = json.loads(request.httprequest.data.decode('utf-8'))

            job = request.env['job.postings'].sudo().browse(job_id)
            if not job.exists():
                return {
                    'status': 404,
                    'error': f'Job with ID {job_id} not found'
                }

            
            updatable_fields = [
                'job_title', 'experience', 'responsibilities',
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
                'status': 201,
                'message': 'Job Updated successfully',
                'job_id': job.id
            }

        except Exception as e:
            return {
                'status': 500,
                'error': f"Internal Server Error: {str(e)}"
            }
            

    
    @http.route('/api/jobs/<string:job_id>', type='json', auth='public', methods=['DELETE'], csrf=False)
    def delete_job(self, job_id, **kwargs):
        """
        Deletes a job posting by the custom job_id (not the internal ID).
        """

        try:
            # Search for job with matching custom job_id field
            job = request.env['job.postings'].sudo().search([('job_id', '=', job_id)], limit=1)

            # If no job is found, return 404
            if not job:
                return {
                    'status': 404,
                    'error': f"No job found with job_id '{job_id}'"
                }

            # Delete the job
            job.unlink()

            return {
                'status': 200,
                'message': f"Job with job_id '{job_id}' has been deleted successfully."
            }

        except Exception as e:
            
            return {
                'status': 500,
                'error': f"Internal Server Error: {str(e)}"
            }
            
            
    @http.route('/api/jobs/<string:job_id>', type='json', auth='public', methods=['PUT'], csrf=False)
    def update_job(self, job_id, **kwargs):
        """
        Update an existing job posting using the custom job_id.
        """
        try:
            # Parse the raw JSON body
            job_data = json.loads(request.httprequest.data.decode('utf-8'))
            if not job_data:
                return {'status': 400, 'error': 'No data provided in the request body.'}
            # Search for the job by custom job_id
            job = request.env['job.postings'].sudo().search([('job_id', '=', job_id)], limit=1)
            if not job:
                return {'status': 404, 'error': f"No job found with job_id '{job_id}'"}
            # Fields allowed to be updated (from your model)
            allowed_fields = [
                'job_title', 'experience', 'responsibilities',
                'requirement', 'skills', 'status', 'workplace_type',
                'shift', 'company', 'location', 'salary',
                'posted_date', 'joining_tentative_date'
            ]
            # Prepare values to update
            update_values = {field: job_data[field] for field in allowed_fields if field in job_data}
            if not update_values:
                return {'status': 400, 'error': 'No valid fields provided for update.'}
            # Write updates to the job record
            job.write(update_values)
            return {
                'status': 200,
                'message': f"Job with job_id '{job_id}' updated successfully.",
                'updated_fields': list(update_values.keys())
            }
        except Exception as e:
            return {'status': 500, 'error': f"Internal Server Error: {str(e)}"}
        """
        Update an existing job posting using the custom job_id field.
        Expects a JSON body with fields to update.
        """
        try:
            # Parse JSON request body
            job_data = request.jsonrequest
            if not job_data:
                return {'status': 400, 'error': 'No data provided in the request body.'}
            # Search for the job using job_id
            job = request.env['job.postings'].sudo().search([('job_id', '=', job_id)], limit=1)
            if not job:
                return {'status': 404, 'error': f"No job found with job_id '{job_id}'"}
            # Define updatable fields from your model
            updatable_fields = [
                'job_title', 'experience', 'responsibilities',
                'requirement', 'skills', 'status', 'workplace_type',
                'shift', 'company', 'location', 'salary',
                'posted_date', 'joining_tentative_date'
            ]
            # Build the dictionary with only valid fields present in request
            update_values = {field: job_data[field] for field in updatable_fields if field in job_data}
            if not update_values:
                return {'status': 400, 'error': 'No valid fields provided to update.'}
            # Write (update) the job
            job.write(update_values)
            return {
                'status': 200,
                'message': f"Job with job_id '{job_id}' updated successfully.",
                'updated_fields': list(update_values.keys())
            }
        except Exception as e:
            return {'status': 500, 'error': f"Internal Server Error: {str(e)}"}
        """
        Create a new job posting (expects raw JSON).
        """
        try:
            # Safely parse raw JSON from the body
            job_data = json.loads(request.httprequest.data.decode('utf-8'))
            job = request.env['job.postings'].sudo().browse(job_id)
            if not job.exists():
                return {
                    'status': 404,
                    'error': f'Job with ID {job_id} not found'
                }
            updatable_fields = [
                'job_title', 'experience', 'responsibilities',
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
                'status': 201,
                'message': 'Job Updated successfully',
                'job_id': job.id
            }
        except Exception as e:
            return {
                'status': 500,
                'error': f"Internal Server Error: {str(e)}"
            }
        

    @http.route('/job', type='http', auth='public', website=True)
    def job_page(self, **kw):
        return request.render('custom_job.job_page_template')

    @http.route('/create-job', type='http', auth='public', website=True)
    def create_job_form(self, **kw):
        return request.render('custom_job.job_form_template')
    
    @http.route('/submit-job', type='http', auth='public', website=True, csrf=False)
    def submit_job(self, **post):
        # Extract form data from 'post'
        job_vals = {
            'job_id': post.get('job_id'),
            'job_title': post.get('job_title'),
            'experience': post.get('experience'),
            'responsibilities': post.get('responsibilities'),
            'requirement': post.get('requirement'),
            'skills': post.get('skills'),
            'status': post.get('status'),
            'workplace_type': post.get('workplace_type'),
            'shift': post.get('shift'),
            'company': post.get('company'),
            'location': post.get('location'),
            'salary': post.get('salary'),
            'posted_date': post.get('posted_date'),
            'joining_tentative_date': post.get('joining_tentative_date'),
        }

        request.env['job.postings'].sudo().create(job_vals)

        return request.redirect('/job')
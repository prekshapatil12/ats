# controllers.py
from odoo import http
from odoo.http import request

class JobController(http.Controller):

    @http.route('/jobs', type='json', auth='public', methods=['GET'], csrf=False)
    def get_jobs(self):
        jobs = request.env['jobs.job'].search([])  
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
                'posted_date': job.posted_date,
                'joining_tentative_date': job.joining_tentative_date,
            })
        return job_list

    @http.route('/jobs/<int:job_id>', type='json', auth='public', methods=['GET'], csrf=False)
    def get_job(self, job_id):
        job = request.env['your_module.job'].search([('job_id', '=', job_id)], limit=1)
        if job:
            return {
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
                'posted_date': job.posted_date,
                'joining_tentative_date': job.joining_tentative_date,
            }
        return {'error': 'Job not found'}

    @http.route('/jobs', type='json', auth='public', methods=['POST'], csrf=False)
    def create_job(self, **kwargs):
        job = request.env['your_module.job'].create({
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
        })
        return {'message': 'Job created successfully', 'job_id': job.job_id}

    @http.route('/jobs/<int:job_id>', type='json', auth='public', methods=['PUT'], csrf=False)
    def update_job(self, job_id, **kwargs):
        job = request.env['your_module.job'].search([('job_id', '=', job_id)], limit=1)
        if job:
            job.write({
                'job_title': kwargs.get('job_title', job.job_title),
                'experience': kwargs.get('experience', job.experience),
                'responsibilities': kwargs.get('responsibilities', job.responsibilities),
                'requirement': kwargs.get('requirement', job.requirement),
                'skills': kwargs.get('skills', job.skills),
                'status': kwargs.get('status', job.status),
                'workplace_type': kwargs.get('workplace_type', job.workplace_type),
                'shift': kwargs.get('shift', job.shift),
                'company': kwargs.get('company', job.company),
                'location': kwargs.get('location', job.location),
                'salary': kwargs.get('salary', job.salary),
                'posted_date': kwargs.get('posted_date', job.posted_date),
                'joining_tentative_date': kwargs.get('joining_tentative_date', job.joining_tentative_date),
            })
            return {'message': 'Job updated successfully'}
        return {'error': 'Job not found'}

    @http.route('/jobs/<int:job_id>', type='json', auth='public', methods=['PATCH'], csrf=False)
    def patch_job(self, job_id, **kwargs):
        job = request.env['your_module.job'].search([('job_id', '=', job_id)], limit=1)
        if job:
            job.write(kwargs)
            return {'message': 'Job patched successfully'}
        return {'error': 'Job not found'}

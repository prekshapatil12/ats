# from odoo import http
# from odoo.http import request
# import json

# class JobAPIController(http.Controller):

# @http.route('/api/jobs', type='json', auth='public', methods=['GET'], csrf=False)
# def get_all_jobs(self):
#         # Fetch all job postings from the job.postings model
#         jobs = request.env['job.postings'].sudo().search([])

#         job_list = []
#         for job in jobs:
#             job_list.append({
#                 'job_id': job.job_id,
#                 'job_title': job.job_title,
#                 'experience': job.experience,
#                 'responsibilities': job.responsibilities,
#                 'requirement': job.requirement,
#                 'skills': job.skills,
#                 'status': job.status,
#                 'workplace_type': job.workplace_type,
#                 'shift': job.shift,
#                 'company': job.company,
#                 'location': job.location,
#                 'salary': job.salary,
#                 'posted_date': str(job.posted_date),
#                 'joining_tentative_date': str(job.joining_tentative_date),
#             })
#         return {'status': 200, 'jobs': job_list}
from odoo import http
from odoo.http import request
import json

@http.route('/api/jobs', auth='public', type='json', methods=['GET'], csrf=False)
def get_jobs(self):
    Job = request.env['custom_job.job_posting'].sudo()  # ✅ no \n
    jobs = Job.search([])
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
            'joining_tentative_date': job.joining_tentative_date
        })
        return {'status': 200, 'jobs': job_list}

@http.route('/api/jobs', auth='public', type='json', methods=['POST'], csrf=False)
def create_job(self, **post):
        job = request.env['custom_job.job_posting'].sudo().create({
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
        })
        return {'status': 'success', 'message': 'Job created successfully', 'id': job.id}

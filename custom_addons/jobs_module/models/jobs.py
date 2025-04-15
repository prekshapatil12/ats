# ats/custom_addons/jobs_module/models/jobs.py

from odoo import models, fields

class Job(models.Model):
    _name = 'ats.jobs'
    _description = 'Job Posting'
    _rec_name = 'title'

    title = fields.Char(string='Job Title', required=True)
    description = fields.Text(string='Job Description')
    department = fields.Char(string='Department')
    location = fields.Char(string='Location')
    date_posted = fields.Date(string='Date Posted', default=fields.Date.today)
    is_active = fields.Boolean(string='Is Active', default=True)

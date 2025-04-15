from odoo import models, fields

class AtsJobs(models.Model):
    _name = 'ats.jobs'          # PostgreSQL table: ats_jobs
    _description = 'ATS Jobs'

    name = fields.Char(string='Job Title', required=True)
    description = fields.Text(string='Job Description')
    location = fields.Char(string='Location')
    department = fields.Char(string='Department')
    is_active = fields.Boolean(string='Is Active', default=True)
    date_posted = fields.Date(string='Date Posted')

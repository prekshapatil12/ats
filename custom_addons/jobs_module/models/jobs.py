from odoo import models, fields

class AtsJob(models.Model):
    _name = 'ats.job'        # Table name in PostgreSQL: ats_job
    _description = 'Job Posting'

    name = fields.Char(string="Job Title", required=True)
    description = fields.Text(string="Job Description")
    location = fields.Char(string="Location")
    job_type = fields.Selection([
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('internship', 'Internship'),
        ('contract', 'Contract')
    ], string="Job Type")
    is_active = fields.Boolean(string="Is Active", default=True)

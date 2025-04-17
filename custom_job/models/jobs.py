from odoo import models, fields

class Job(models.Model):
    _name = 'custom.job'
    _description = 'Mapped Job Table'
    _table = 'jobs'

    title = fields.Char(required=True)
    description = fields.Text(required=True)
    location = fields.Char()
    job_type = fields.Char()
    department = fields.Char()
    salary_range = fields.Char()
    is_remote = fields.Boolean()
    posted_by = fields.Char()
    created_at = fields.Datetime()
    updated_at = fields.Datetime()

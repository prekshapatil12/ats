from odoo import models, fields

class Job(models.Model):
    _name = 'custom.job'
    _description = 'Job Posting'

    name = fields.Char(string='Job Title', required=True)
    department = fields.Char(string='Department')
    description = fields.Text(string='Description')
    is_active = fields.Boolean(string='Active', default=True)
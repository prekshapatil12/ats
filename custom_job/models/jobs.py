from odoo import models, fields

class JobListing(models.Model):
    _name = 'custom.job'
    _description = 'Job Listing'

    name = fields.Char(string='Job Title', required=True)
    location = fields.Char(string='Location')
    department = fields.Char(string='Department')
    description = fields.Text(string='Job Description')
    requirements = fields.Text(string='Requirements')
    is_published = fields.Boolean(string='Published', default=True)

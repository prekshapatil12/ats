# # models/job.py
# from odoo import models, fields

# class Job(models.Model):
#     _name = 'job.postings'  # Odoo model name
#     _table = 'job_postings'  # This is the PostgreSQL table name you're working with

#     job_id = fields.Integer(string='Job ID', required=True)
#     job_title = fields.Char(string='Job Title')
#     experience = fields.Char(string='Experience')
#     responsibilities = fields.Text(string='Responsibilities')
#     requirement = fields.Text(string='Requirement')
#     skills = fields.Char(string='Skills')
#     status = fields.Selection([('t', 'Open'), ('f', 'Closed')], string='Status')
#     workplace_type = fields.Selection([('Remote', 'Remote'), ('Hybrid', 'Hybrid'), ('On-Site', 'On-Site')], string='Workplace Type')
#     shift = fields.Selection([('Day', 'Day'), ('Evening', 'Evening')], string='Shift')
#     company = fields.Char(string='Company')
#     location = fields.Char(string='Location')
#     salary = fields.Float(string='Salary')
#     posted_date = fields.Date(string='Posted Date')
#     joining_tentative_date = fields.Date(string='Joining Tentative Date')

# models/job.py
# models/job.py
from odoo import models, fields

class JobPosting(models.Model):
    _name = 'job.postings'
    _description = 'Job Posting'
    _table = 'job_postings'  # Ensure that this table has the 'id' column.

    job_id = fields.Char(string="Job ID", required=True)
    job_title = fields.Char(string="Job Title", required=True)
    experience = fields.Char(string="Experience")
    responsibilities = fields.Text(string="Responsibilities")
    requirement = fields.Text(string="Requirement")
    skills = fields.Char(string="Skills")
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string="Status", default='active')
    workplace_type = fields.Selection([('remote', 'Remote'), ('onsite', 'On-site'), ('hybrid', 'Hybrid')], string="Workplace Type")
    shift = fields.Char(string="Shift")
    company = fields.Char(string="Company")
    location = fields.Char(string="Location")
    salary = fields.Char(string="Salary")
    posted_date = fields.Date(string="Posted Date")
    joining_tentative_date = fields.Date(string="Joining Tentative Date")

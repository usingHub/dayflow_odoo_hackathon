from odoo import models, fields

class DayflowEmployee(models.Model):
    _inherit = 'hr.employee'  # extend Odoo's hr.employee

    # Extra fields for Dayflow
    date_of_birth = fields.Date(string="Date of Birth")
    emergency_contact = fields.Char(string="Emergency Contact")
    # Add other hackathon-specific fields here

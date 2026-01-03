from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    # Non-critical fields (Employee can edit via API – enforced later)
    personal_phone = fields.Char(
        string="Personal Phone"
    )

    personal_address = fields.Text(
        string="Personal Address"
    )

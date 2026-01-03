from odoo import models, fields


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    status = fields.Selection(
        [
            ("present", "Present"),
            ("half_day", "Half Day"),
            ("absent", "Absent"),
        ],
        string="Attendance Status",
        default="present",
    )

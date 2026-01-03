from odoo import models, fields, api
from datetime import datetime

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

    @api.model
    def action_check_in(self, employee_id):
        """Create a new check-in record for the employee"""
        return self.create({
            'employee_id': employee_id,
            'check_in': fields.Datetime.now(),
            'status': 'present'
        })

    def action_check_out(self):
        """Update the last open attendance record with check-out"""
        for record in self:
            if record.check_out:
                continue  # Already checked out
            record.check_out = fields.Datetime.now()
            # Optional: auto-set status to half_day if < 4 hours
            if record.check_in and record.check_out:
                delta = record.check_out - record.check_in
                hours = delta.total_seconds() / 3600
                if hours < 4:
                    record.status = 'half_day'

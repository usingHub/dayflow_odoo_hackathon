from odoo import models, fields


class HrLeave(models.Model):
    _inherit = "hr.leave"

    leave_type = fields.Selection(
        [
            ("paid", "Paid Leave"),
            ("sick", "Sick Leave"),
        ],
        string="Leave Type",
        required=True,
        default="paid",
    )

    manager_comment = fields.Text(
        string="Manager Comment"
    )

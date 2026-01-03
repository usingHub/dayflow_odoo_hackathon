from odoo import http
from odoo.http import request


class DayflowAPI(http.Controller):

    @http.route("/api/employee/profile", type="json", auth="user")
    def employee_profile(self):
        employee = request.env["hr.employee"].search(
            [("user_id", "=", request.env.user.id)], limit=1
        )
        return {
            "id": employee.id,
            "name": employee.name,
            "phone": employee.personal_phone,
            "address": employee.personal_address,
        }

    @http.route("/api/attendance", type="json", auth="user")
    def attendance_list(self):
        employee = request.env["hr.employee"].search(
            [("user_id", "=", request.env.user.id)], limit=1
        )
        attendances = request.env["hr.attendance"].search_read(
            [("employee_id", "=", employee.id)],
            ["check_in", "check_out", "status"],
            limit=50,
        )
        return attendances

    @http.route("/api/leaves", type="json", auth="user")
    def leave_list(self):
        leaves = request.env["hr.leave"].search_read(
            [("employee_id.user_id", "=", request.env.user.id)],
            ["request_date_from", "request_date_to", "state", "leave_type"],
            limit=50,
        )
        return leaves

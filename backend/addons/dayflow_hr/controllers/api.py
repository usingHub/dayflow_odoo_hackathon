from odoo import http
from odoo.http import request
from odoo.exceptions import AccessError
from datetime import datetime


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
    
class DayflowAPI(http.Controller):

    @http.route("/api/attendance/check_in", type="json", auth="user")
    def check_in(self):
        employee = request.env["hr.employee"].search(
            [("user_id", "=", request.env.user.id)], limit=1
        )
        if not employee:
            raise AccessError("Employee not found")

        open_attendance = request.env["hr.attendance"].search(
            [("employee_id", "=", employee.id), ("check_out", "=", False)],
            limit=1,
        )
        if open_attendance:
            return {"error": "Already checked in"}

        request.env["hr.attendance"].create({
            "employee_id": employee.id,
            "check_in": datetime.now(),
        })
        return {"status": "checked_in"}

    @http.route("/api/attendance/check_out", type="json", auth="user")
    def check_out(self):
        employee = request.env["hr.employee"].search(
            [("user_id", "=", request.env.user.id)], limit=1
        )
        attendance = request.env["hr.attendance"].search(
            [("employee_id", "=", employee.id), ("check_out", "=", False)],
            limit=1,
        )
        if not attendance:
            return {"error": "No active check-in"}

        attendance.write({"check_out": datetime.now()})
        return {"status": "checked_out"}
    
    @http.route("/api/leave/apply", type="json", auth="user")
    def apply_leave(self, **data):
        employee = request.env["hr.employee"].search(
            [("user_id", "=", request.env.user.id)], limit=1
        )

        leave = request.env["hr.leave"].create({
            "employee_id": employee.id,
            "request_date_from": data.get("date_from"),
            "request_date_to": data.get("date_to"),
            "leave_type": data.get("leave_type", "paid"),
        })
        return {"id": leave.id, "status": "submitted"}
    
    @http.route("/api/leave/action", type="json", auth="user")
    def leave_action(self, **data):
        if not request.env.user.has_group("hr.group_hr_manager"):
            raise AccessError("Not allowed")

        leave = request.env["hr.leave"].browse(data.get("leave_id"))
        leave.write({
            "state": data.get("action"),  # approve / refuse
            "manager_comment": data.get("comment"),
        })
        return {"status": "updated"}


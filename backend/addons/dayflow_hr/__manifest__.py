{
    "name": "Dayflow HRMS",
    "version": "1.0.0",
    "summary": "Lightweight HRMS for attendance, leave, and payroll management",
    "description": """
        Dayflow is a streamlined HRMS designed for hackathons and small teams.
        It provides employee management, attendance tracking, leave workflows,
        and transparent payroll calculations with role-based access control.
    """,
    "author": "Dayflow Team",
    "category": "Human Resources",
    "depends": [
        "base",
        "hr",              # Employee data
        "hr_contract",     # Salary / Wage
        "hr_attendance",   # Check-in / Check-out
        "hr_holidays",     # Leave / Time-off
    ],
    "data": [
        #"security/security.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}

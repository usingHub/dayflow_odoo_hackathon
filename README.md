
 DayFlow HRM – Odoo 17 Based HR Solution

 Problem Statement

Building a full-featured HR system from scratch within a hackathon timeline is impractical due to complexity around payroll, attendance, security, and workflows.

 Solution

DayFlow HRM extends Odoo 17, an open-source ERP, to deliver a scalable and production-ready HR Management system by customizing core HR modules instead of reinventing them.

---

 Tech Stack

 Odoo 17 (Python ORM, Modular Framework)
 PostgreSQL (via Odoo)
 XML (Views & Config)
 Git

---

 Key Features

 Employee Management (hr.employee)
 Attendance Extension (hr.attendance)

   Added attendance status: Present / Half Day / Absent
 Leave Management (hr.leave)

   Leave Type (Paid / Sick)
   Manager Comment
 Salary Structure Logic (hr.contract)

   Automatic wage breakup (Basic, HRA, Bonus, LTA, Allowances)

All features are implemented using model inheritance, ensuring upgrade safety.

---

 Challenges & How We Solved Them

 Odoo setup & config issues (addons path, odoo.conf, web module)

   Resolved via proper configuration and dependency handling
 XML/View errors during module upgrades

   Temporarily disabled non-critical views to prioritize backend stability
 Security & access control

   Used default Odoo roles; custom ACLs can be added later without refactoring

AI assistance was used as a debugging and learning aid, while all architectural and implementation decisions were made by the team.

---

 Why Odoo?

 Open-source & free
 Enterprise-grade HR modules
 Secure ORM and workflows
 Highly modular and scalable
 Ideal for rapid development under time constraints

---

 Why No Custom Frontend?

 Odoo provides a complete backend UI
 Focus was on business logic and correctness
 External frontend (web/mobile) can be added later using Odoo APIs

---

 Scalability

 Modular design
 Easy to extend with Payroll, Approvals, ACLs, Dashboards
 Ready for production-level growth

---

 Final Outcome

A working HR system with employees, attendance, leave, and salary logic, built quickly, cleanly, and scalable — proving that leveraging the right platform beats rebuilding everything from scratch.


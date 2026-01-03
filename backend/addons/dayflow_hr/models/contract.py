from odoo import models, fields, api


class HrContract(models.Model):
    _inherit = "hr.contract"

    basic = fields.Float(compute="_compute_salary", store=False)
    hra = fields.Float(compute="_compute_salary", store=False)
    standard_allowance = fields.Float(
        default=4167, store=False
    )
    bonus = fields.Float(compute="_compute_salary", store=False)
    lta = fields.Float(compute="_compute_salary", store=False)
    fixed_allowance = fields.Float(compute="_compute_salary", store=False)

    @api.depends("wage")
    def _compute_salary(self):
        for record in self:
            wage = record.wage or 0.0

            basic = wage * 0.50
            hra = basic * 0.50
            bonus = wage * 0.0833
            lta = wage * 0.0833

            record.basic = basic
            record.hra = hra
            record.bonus = bonus
            record.lta = lta
            record.fixed_allowance = (
                wage
                - (basic + hra + record.standard_allowance + bonus + lta)
            )

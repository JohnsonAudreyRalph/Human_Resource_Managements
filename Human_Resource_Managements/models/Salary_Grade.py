# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SalaryGrade(models.Model):
    _name = 'salary.grade'
    _inherit = 'mail.thread',
    _description = 'Quản lý mức lương'
    _rec_name = 'Salary_Grade_ID'

    Salary_Grade_ID = fields.Char(string='Mã mức lương', default=lambda self: _('Tạo thông tin mới'))
    Basic_Salary = fields.Char(string='Mức lương cơ bản', required=True, tracking=True)
    Salary_Coefficient = fields.Char(string='Hệ số lương', required=True, tracking=True)
    Allowance_Coefficient = fields.Char(string='Hệ số phụ cấp', required=True, tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['Salary_Grade_ID'] = self.env['ir.sequence'].next_by_code('salary.grade')
        return super(SalaryGrade, self).create(vals_list)

# Bộ phận phòng ban làm việc
# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class DepartmentInformation(models.Model):
    _name = 'department.information'
    _inherit = 'mail.thread',
    _description = 'Bộ phận phòng ban'
    _rec_name = 'Department_ID'

    Department_ID = fields.Char(string='Mã phòng ban', default=lambda self: _('Tạo thông tin mới'))
    Name_Department = fields.Char(string='Tên phòng ban', required=True, tracking=True)
    Address_Department = fields.Char(string='Địa chỉ phòng ban', required=True, tracking=True)
    Phone_Number_Department = fields.Char(string='Số điện thoại phòng ban', required=True, tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['Department_ID'] = self.env['ir.sequence'].next_by_code('department.information')
        return super(DepartmentInformation, self).create(vals_list)

    def name_get(self):
        result = []
        for rec in self:
            name = f'{rec.Department_ID} - {rec.Name_Department} '
            result.append((rec.id, name))
        return result

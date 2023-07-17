# Quản lý thông tin nhân viên
# -*- coding: utf-8 -*-
from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class EmployeeInformation(models.Model):
    _name = 'employee.information'
    _inherit = 'mail.thread',
    _description = 'Thông tin nhân viên'

    Employee_ID = fields.Char(string='Mã nhân viên', default=lambda self: _('Tạo thông tin mới'))
    name = fields.Char(string='Họ và tên', required=True, tracking=True)
    Age = fields.Integer(string='Tuổi',
                         required=True,
                         tracking=True,
                         compute='_compute_auto_calculator_age')
    Gender = fields.Selection([('Male', 'Nam'), ('Female', 'Nữ'), ('Others', 'Khác')], string='Giới tính', required=True, tracking=True)
    Address = fields.Text(string='Địa chỉ', required=True, tracking=True)
    Date = fields.Date(string='Ngày sinh', required=True, tracking=True)
    Email = fields.Char(string='Email', required=True, tracking=True)
    Phone_Number = fields.Char(string='Số điện thoại', required=True, tracking=True)
    Ethnicity = fields.Char(string='Dân tộc', required=True, tracking=True)
    Department_ID = fields.Many2one(
        "department.information",
        string='Mã phòng ban',
        required=True,
        tracking=True
    )
    Position_ID = fields.Many2one(
        "position.information",
        string='Mã chức vụ',
        required=True,
        tracking=True
    )
    Education_Level_ID = fields.Many2one(
        "education.level",
        string='Mã trình độ học vấn',
        required=True,
        tracking=True
    )
    Salary_Grade_ID = fields.Many2one(
        "salary.grade",
        string='Bậc lương',
        required=True,
        tracking=True
    )

    active = fields.Boolean(default=True)
    priority = fields.Selection([
        ('0', ''),
        ('1', 'Thấp'),
        ('2', 'Thường'),
        ('3', 'Cao'),
        ('4', 'Rất cao')], string="Đánh giá hiệu xuất")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['Employee_ID'] = self.env['ir.sequence'].next_by_code('employee.information')
        return super(EmployeeInformation, self).create(vals_list)

    @api.depends('Date')
    def _compute_auto_calculator_age(self):
        for record in self:
            today = date.today()
            if record.Date:
                record.Age = today.year - record.Date.year
                if record.Age == 0:
                    raise ValidationError("Lỗi. Độ tuổi nhập không đúng╰(*°▽°*)╯")
            else:
                record.Age = 0

    @api.constrains('Email')
    def _validate_email(self):
        for record in self:
            if record.Email and '@' not in record.Email:
                raise ValidationError("Địa chỉ email không hợp lệ!")

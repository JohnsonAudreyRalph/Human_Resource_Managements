# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class EducationLevel(models.Model):
    _name = 'education.level'
    _inherit = 'mail.thread',
    _description = 'Trình độ học vấn'

    Education_Level_ID = fields.Char(string='Mã trình độ học vấn', default=lambda self: _('Tạo thông tin mới'))
    Name = fields.Char(string='Trình độ', required=True, tracking=True)
    Major = fields.Char(string='Chuyên ngành', required=True, tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['Education_Level_ID'] = self.env['ir.sequence'].next_by_code('education.level')
        return super(EducationLevel, self).create(vals_list)

    def name_get(self):
        result = []
        for rec in self:
            name = f'{rec.Education_Level_ID} - {rec.Name} '
            result.append((rec.id, name))
        return result

# Quản lý chức vụ
# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class PositionInformation(models.Model):
    _name = 'position.information'
    _inherit = 'mail.thread',
    _description = 'Quản lý chức vụ'
    _rec_name = 'Position_ID'

    Position_ID = fields.Char(string='Mã chức vụ', default=lambda self: _('Tạo thông tin mới'))
    Name = fields.Char(string='Tên chức vụ', required=True, tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['Position_ID'] = self.env['ir.sequence'].next_by_code('position.information')
        return super(PositionInformation, self).create(vals_list)

    def name_get(self):
        result = []
        for rec in self:
            name = f'{rec.Position_ID} - {rec.Name} '
            result.append((rec.id, name))
        return result

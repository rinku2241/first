
# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Studentclass(models.Model):
    _name = 'schoool.student'

    name = fields.Char()
    roll_no = fields.Integer()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

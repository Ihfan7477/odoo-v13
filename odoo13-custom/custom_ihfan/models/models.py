# -*- coding: utf-8 -*-

from dataclasses import field
from odoo import api, fields, models, exceptions

class custom_ihfan(models.Model):
     _inherit = 'sale.order'
     request_vendor = fields.Many2one('res.partner', string='request vendor')
     no_kontrak = fields.Char(string='no kontrak')
     with_PO = fields.Boolean(string='with PO')
#     _name = 'custom_ihfan.custom_ihfan'
#     _description = 'custom_ihfan.custom_ihfan'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

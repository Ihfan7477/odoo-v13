# -*- coding: utf-8 -*-
# from odoo import http


# class CustomIhfan(http.Controller):
#     @http.route('/custom_ihfan/custom_ihfan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_ihfan/custom_ihfan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_ihfan.listing', {
#             'root': '/custom_ihfan/custom_ihfan',
#             'objects': http.request.env['custom_ihfan.custom_ihfan'].search([]),
#         })

#     @http.route('/custom_ihfan/custom_ihfan/objects/<model("custom_ihfan.custom_ihfan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_ihfan.object', {
#             'object': obj
#         })

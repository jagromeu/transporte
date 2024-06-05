# -*- coding: utf-8 -*-
# from odoo import http


# class Transporte(http.Controller):
#     @http.route('/transporte/transporte/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/transporte/transporte/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('transporte.listing', {
#             'root': '/transporte/transporte',
#             'objects': http.request.env['transporte.transporte'].search([]),
#         })

#     @http.route('/transporte/transporte/objects/<model("transporte.transporte"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('transporte.object', {
#             'object': obj
#         })

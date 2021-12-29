# -*- coding: utf-8 -*-
# from odoo import http


# class CustomVar/contactsSiic(http.Controller):
#     @http.route('/custom_var/contacts_siic/custom_var/contacts_siic/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_var/contacts_siic/custom_var/contacts_siic/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_var/contacts_siic.listing', {
#             'root': '/custom_var/contacts_siic/custom_var/contacts_siic',
#             'objects': http.request.env['custom_var/contacts_siic.custom_var/contacts_siic'].search([]),
#         })

#     @http.route('/custom_var/contacts_siic/custom_var/contacts_siic/objects/<model("custom_var/contacts_siic.custom_var/contacts_siic"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_var/contacts_siic.object', {
#             'object': obj
#         })

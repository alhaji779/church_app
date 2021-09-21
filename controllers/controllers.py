# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, route

# class ChurchApp(http.Controller):
#     @http.route('/church_app/church_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/church_app/church_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('church_app.listing', {
#             'root': '/church_app/church_app',
#             'objects': http.request.env['church_app.church_app'].search([]),
#         })

#     @http.route('/church_app/church_app/objects/<model("church_app.church_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('church_app.object', {
#             'object': obj
#         })

class res(http.Controller):
    @route('/account_payment/account_payment/pay/', website=True, auth="public")
    def invoice_pay_form(self, **kwargs):
            return http.request.render('church_app.res', {})
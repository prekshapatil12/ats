from odoo import http
from odoo.http import request

class RestApiDemo(http.Controller):

    @http.route('/api/partners', auth='public', type='json', methods=['GET'], csrf=False)
    def get_partners(self):
        partners = request.env['res.partner'].sudo().search([], limit=10)
        return [
            {
                'id': p.id,
                'name': p.name,
                'email': p.email
            } for p in partners
        ]

    @http.route('/api/partners', auth='public', type='json', methods=['POST'], csrf=False)
    def create_partner(self, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        if not name:
            return {'error': 'Name is required'}
        partner = request.env['res.partner'].sudo().create({
            'name': name,
            'email': email
        })
        return {
            'id': partner.id,
            'name': partner.name,
            'email': partner.email
        }
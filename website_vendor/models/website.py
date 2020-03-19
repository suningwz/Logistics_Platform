#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Website(models.Model):
    _inherit = 'website'

    @api.model
    def get_logistics_user_type(self):
        type_ids = self.env['logistics.user.type'].sudo().search([])
        return type_ids

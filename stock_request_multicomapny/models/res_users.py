# -*- coding: utf-8 -*-

from odoo import models, fields


class Users(models.Model):
    _inherit = "res.users"

    custom_inventory_allowed_companies = fields.Many2many(
        'res.company',
        string="Allowed Inventory Companies",
    )

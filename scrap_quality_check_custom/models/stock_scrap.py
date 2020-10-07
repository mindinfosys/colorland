# -*- coding: utf-8 -*-
from odoo import fields, models


class StockScrap(models.Model):
    _inherit = "stock.scrap"

    quality_check = fields.Boolean(
        string="Quality Check",
        copy=False
    )

    def custom_quality_check(self):
    	self.quality_check = True
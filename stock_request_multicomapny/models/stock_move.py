# -*- coding: utf-8 -*-

from odoo import models


class StockMove(models.Model):
    _inherit = "stock.move"

    def _check_company(self, fnames=None):
        if self._context.get("custom_stock_request_confirm"):
            return
        return super(StockMove, self)._check_company(fnames)


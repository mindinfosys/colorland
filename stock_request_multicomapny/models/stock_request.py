# -*- coding: utf-8 -*-

from odoo import models, api


class StockRequest(models.Model):
    _inherit = "stock.request"

    def _action_launch_procurement_rule(self):
        return super(StockRequest, self.with_context(custom_stock_request_confirm=True))._action_launch_procurement_rule()
    
    @api.depends("allocation_ids")
    def _compute_picking_ids(self):
        res = super(StockRequest, self)._compute_picking_ids()
        for request in self:
            back_picking_ids = self.env['stock.picking'].search([('origin', '=', request.order_id.name)])
            if back_picking_ids:
                request.picking_ids += back_picking_ids
            request.picking_count = len(request.picking_ids)

# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, SUPERUSER_ID


class StockQuant(models.Model):
    _inherit = "stock.quant"
    
    custom_barcode = fields.Char(
        string='Bardcode',
        related='product_id.barcode',
    )
    custom_sale_price = fields.Float(
        string='Sale Price',
        related='product_id.lst_price',
    )
    custom_cost_price = fields.Float(
        string='Cost Price',
        related='product_id.standard_price',
    )

    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        if self._context.get('custom_inventory_company_ids'):
            args += [('company_id', 'in', self.env.user.custom_inventory_allowed_companies.ids), ('location_id.active', '=', True)]
            access_rights_uid = SUPERUSER_ID
            return super(StockQuant, self.sudo())._search(args, offset=offset, limit=limit, order=order, count=count, access_rights_uid=access_rights_uid)
        return super(StockQuant, self)._search(args, offset=offset, limit=limit, order=order, count=count, access_rights_uid=access_rights_uid)
    
    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        if self._context.get('custom_inventory_company_ids'):
            domain += [('company_id', 'in', self.env.user.custom_inventory_allowed_companies.ids), ('location_id.active', '=', True)]
            return super(StockQuant, self.sudo()).search_read(domain, fields, offset, limit, order)
        return super(StockQuant, self).search_read(domain, fields, offset, limit, order)
    
    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        if self._context.get('custom_inventory_company_ids'):
            domain += [('company_id', 'in', self.env.user.custom_inventory_allowed_companies.ids), ('location_id.active', '=', True)]
            return super(StockQuant, self.sudo()).read_group(domain, fields, groupby, offset, limit, orderby, lazy)
        return super(StockQuant, self).read_group(domain, fields, groupby, offset, limit, orderby, lazy)

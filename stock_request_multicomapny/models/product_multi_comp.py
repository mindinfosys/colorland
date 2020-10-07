# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        compute="_compute_company_id",
        search="_search_company_id",
    )

    custom_inventory_allowed_companies = fields.Many2many(
        'res.company',
        'product_template_company_invent_rel',
        'product_tmpl_id',
        'company_id',
        string="Allowed Inventory Companies",
        default=lambda self: self._default_company_ids(),
    )

    def _default_company_ids(self):
        return self.browse(self.env.company.ids)

    @api.depends("custom_inventory_allowed_companies")
    def _compute_company_id(self):
        for record in self:
            # Give the priority of the current company of the user to avoid
            # multi company incompatibility errors.
            company_id = self.env.context.get("force_company") or self.env.company.id
            if company_id in record.custom_inventory_allowed_companies.ids:
                record.company_id = company_id
            else:
                record.company_id = record.custom_inventory_allowed_companies[:1].id

    def _search_company_id(self, operator, value):
        return [("custom_inventory_allowed_companies", operator, value)]

    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        args += ['|', ('custom_inventory_allowed_companies', 'in', self.env.user.custom_inventory_allowed_companies.ids),('custom_inventory_allowed_companies', 'in', self.env.user.company_id.ids)]
        return super(ProductTemplate, self)._search(args, offset=offset, limit=limit, order=order, count=count, access_rights_uid=access_rights_uid)


class Product(models.Model):
    _inherit = 'product.product'

    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        args += ['|', ('custom_inventory_allowed_companies', 'in', self.env.user.custom_inventory_allowed_companies.ids),('custom_inventory_allowed_companies', 'in', self.env.user.company_id.ids)]
        return super(Product, self)._search(args, offset=offset, limit=limit, order=order, count=count, access_rights_uid=access_rights_uid)

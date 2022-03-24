# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def get_description_following_lines(self):
        res = super(SaleOrderLine, self).get_description_following_lines()
        if self.product_packaging and self.product_packaging.uom_id and self.product_packaging.uom_id.factor_inv > 1:
            res.append(_('Package of ') + str(int(self.product_packaging.uom_id.factor_inv)))
        return res

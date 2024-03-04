#-- coding: utf-8 --

from odoo import models, fields, api

class StockPickingInherit(models.Model):
    _inherit = "stock.picking"

    volume = fields.Float(compute="_compute_volume", store=True)

    @api.depends("product_id")
    def _compute_volume(self):
        vulume = 0
        for product in self.product_id:
            vulume += product.volume

        self.volume = vulume
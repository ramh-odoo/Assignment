#-- coding: utf-8 --

from odoo import models, fields, api

class StockPickingInherit(models.Model):
    _inherit = "stock.picking"

    volume = fields.Float(compute="_compute_volume")

    @api.depends('move_line_ids')
    def _compute_volume(self):
        for record in self:
            record.volume = sum(move_line.product_id.volume for move_line in record.move_line_ids if move_line.product_id )

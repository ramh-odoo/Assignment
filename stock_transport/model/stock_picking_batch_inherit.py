#-*- coding: utf-8 -*-

from odoo import fields, models, api

class StockPickingBatchInherit(models.Model):
    _inherit = 'stock.picking.batch'

    dock = fields.Many2one('dock', string='Dock')
    vehicle = fields.Many2one('fleet.vehicle.model')
    vehicle_category = fields.Many2one('fleet.vehicle.model.category', string='Vehicle Category')
    weight = fields.Float(compute="_compute_weight", store=True)
    volume = fields.Float(compute="_compute_volume", store=True)
    total_weight = fields.Float(compute="_compute_weight")
    total_volume = fields.Float(compute="_compute_volume")
    transfers = fields.Float(compute="_compute_lines_transfers", store=True)
    lines = fields.Float(compute="_compute_lines_transfers", store=True)

    @api.depends('move_ids', 'vehicle_category', 'move_line_ids')
    def _compute_weight(self):
        for record in self:
            max_weight = record.vehicle_category.max_weight or 1
            current_weight = sum(move.product_qty * move.product_id.weight for move in record.move_ids)
            record.weight = min((current_weight / max_weight) * 100, 100)
            record.total_weight = current_weight

    @api.depends('move_ids', 'vehicle_category', 'move_line_ids')
    def _compute_volume(self):
        for record in self:
            max_volume = record.vehicle_category.max_volume or 1
            current_volume = sum(move.product_qty * move.product_id.volume for move in record.move_ids)
            record.volume = min((current_volume / max_volume) * 100, 100)
            record.total_volume = current_volume
    
    @api.depends('move_line_ids','picking_ids')
    def _compute_lines_transfers(self):
        for record in self:
            record.transfers = len(record.picking_ids)
            record.lines= len(record.move_line_ids)

#-*- coding: utf-8 -*-

from odoo import fields, models, api

class StockPickingBatchInherit(models.Model):
    _inherit = 'stock.picking.batch'

    dock = fields.Many2one('dock', string='Dock')
    vehicle = fields.Many2one('fleet.vehicle.model', string='Third Party Provider')
    vehicle_category = fields.Many2one('fleet.vehicle.model.category', string='Vehicle Category', placeholder='e.g. Semi-truck')
    weight = fields.Float(compute="_compute_weight", store=True)
    volume = fields.Float(compute="_compute_volume", store=True)


    @api.depends('move_ids','vehicle_category','move_line_ids')
    def _compute_weight(self):
        for record in self:
            max_weight = record.vehicle_category.max_weight
            current_weight = 0
            for move_id in record.move_ids:
                current_weight  += move_id.product_qty*move_id.product_id.weight

            if  max_weight:
                record.weight = (current_weight / max_weight)*100
            else:
                record.weight = 1

            if record.weight>100:
                record.weight = 100


    @api.depends('move_ids','vehicle_category','move_line_ids')
    def _compute_volume(self):
        for record in self:
            max_volume = record.vehicle_category.max_volume
            current_volume = 0
            for move_id in record.move_ids:
                current_volume += move_id.product_qty*move_id.product_id.volume

            if max_volume:
                record.volume = (current_volume / max_volume)*100
            else:
                record.volume = 1

            if record.volume>100:
                record.volume = 100



    
    # @api.depends('picking_ids','vehicle_category', 'move_line_ids.product_id','move_line_ids')
    # def _compute_weight_volume(self):
    #     computed_weight =0
    #     computed_volume =0
    #     move_line_ids = self.move_line_ids
    #     all_product_ids = self.move_line_ids.mapped('product_id').ids
    #     products = self.env['product.product'].browse(all_product_ids)
    #     if len(products) >0:
    #         for product in products:
    #             computed_weight += product.weight
    #             computed_volume += product.volume
    #     self.weight = computed_weight
    #     self.volume = computed_volume

    # @api.depends('picking_ids','vehicle_category','move_line_ids')
    # def _compute_weight_volume(self):
    #     computed_weight =0
    #     computed_volume =0
    #     if self.vehicle_category:
    #         max_weight = self.vehicle_category.max_weight
    #         max_volume = self.vehicle_category.max_volume
    #         picking_ids = []
    #         for picking in self.picking_ids:
    #             picking_ids.append(picking)

    #         for product in picking_ids:
    #             computed_weight += product.weight
    #             computed_volume += product.volume

    #         self.weight = computed_weight / max_weight *100 if max_weight else computed_weight
    #         self.volume = computed_volume / max_volume *100 if max_volume else computed_volume


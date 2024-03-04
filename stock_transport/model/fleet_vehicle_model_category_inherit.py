#-*- coding: utf-8 -*-

from odoo import fields, models,api

class FleetVehicleModelCategoryInherit(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Float(string='Max Weight (kg)')
    max_volume = fields.Float(string='Max Volume (m³)')

    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({str(record.max_weight)}kg, {str(record.max_volume)}m³)"


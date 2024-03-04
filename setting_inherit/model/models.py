from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_stock_transport = fields.Boolean(string='Install Stock Transport Module')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            module_stock_transport=self.env['ir.config_parameter'].sudo().get_param('setting_inherit.module_stock_transport')
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('setting_inherit.module_stock_transport', self.module_stock_transport)

        if self.module_stock_transport:
            # Install the stock_transport module
            stock_transport_module = self.env['ir.module.module'].sudo().search([('name', '=', 'stock_transport')], limit=1)
            if stock_transport_module:
                stock_transport_module.button_immediate_install()

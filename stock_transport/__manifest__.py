#-*- coding: utf-8 -*-

{
    "name": "Stock Transport",
    "description": "A project for setting inherit",
    "summary": "Stock setting Project",
    "category" : "industry",
    "installable": True,
    "application": True,
    "license": "OEEL-1",
    "version": "1.0",
    "depends": ["base","stock_picking_batch", "fleet" ],
    "data" : [
        "views/fleet_vehicle_category_views_inherit.xml",
        "views/stock_picking_batch_views_inherit.xml",
        "views/stock_picking_views_inherit.xml",
    ]
}

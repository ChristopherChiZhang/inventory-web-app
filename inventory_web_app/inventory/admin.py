from django.contrib import admin

from inventory.models import Product, Shipment

admin.site.register(Product)
admin.site.register(Shipment)

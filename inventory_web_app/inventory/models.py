from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    sku = models.CharField(max_length=12, unique=True)
    description = models.CharField(max_length=255, null=False)
    quantity = models.IntegerField(default=0)
    shipment = models.ForeignKey('Shipment', related_name='products', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'inventory_products'


class Shipment(models.Model):
    name = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'inventory_shipments'

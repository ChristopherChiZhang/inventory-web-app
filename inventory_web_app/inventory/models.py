from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    sku = models.IntegerField(max_length=12, unique=True)
    description = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'inventory_products'


class Shipment(models.Model):
    name = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'inventory_shipments'

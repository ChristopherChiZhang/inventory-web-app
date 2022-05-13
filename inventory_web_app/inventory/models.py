from django.db import models

from django.db import models


class Timestamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    objects = models.Manager()

    class Meta:
        abstract = True


class Product(Timestamped):
    name = models.CharField(max_length=255, null=False)
    sku = models.CharField(max_length=12, unique=True)
    description = models.CharField(max_length=255, null=False)
    quantity = models.IntegerField(default=0)
    shipment = models.ForeignKey('Shipment', related_name='products', on_delete=models.SET_NULL, null=True, blank=True)

    objects = models.Manager()

    class Meta:
        db_table = 'inventory_products'

    def __str__(self):
        return f'{self.name} ({self.sku})'


class Shipment(Timestamped):
    name = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'inventory_shipments'

    def __str__(self):
        return self.name

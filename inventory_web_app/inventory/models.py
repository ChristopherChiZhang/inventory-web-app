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

    objects = models.Manager()

    class Meta:
        db_table = 'inventory_products'

    def __str__(self):
        return f'{self.name} ({self.sku})'

    def update_quantity(self, quantity_to_remove):
        if self.quantity - quantity_to_remove >= 0:
            self.quantity -= quantity_to_remove
            self.save()
            return True

        return False


class Shipment(Timestamped):
    name = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'inventory_shipments'

    def __str__(self):
        return self.name

    @classmethod
    def create_shipment(cls, name):
        return Shipment.objects.create(name=name)


class ShipmentItem(Timestamped):
    shipment = models.ForeignKey('Shipment', related_name='shipment_items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=225)
    quantity_shipped = models.IntegerField()

    @classmethod
    def create_shipment_item(cls, shipment, name, quantity_shipped):
        ShipmentItem.objects.create(shipment=shipment, product_name=name, quantity_shipped=quantity_shipped)

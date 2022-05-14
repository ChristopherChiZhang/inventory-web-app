from django.db import migrations


def forward(apps, schema_editor):
    """
    Create some products to populate the product table.
    """
    Product = apps.get_model('inventory', 'Product')
    products_to_create = [
        {'name': 'Surgical Gloves', 'sku': '1111111111', 'description': 'Standard blue latex gloves for dentists.',
         'quantity': 10000},
        {'name': 'Bar Soap', 'sku': '2222222222', 'description': 'Standard soap for washing hands.',
         'quantity': 200},
        {'name': 'Dish Soap', 'sku': '3333333333', 'description': 'Standard soap used to wash dishes.',
         'quantity': 60000},
        {'name': 'Dental Floss', 'sku': '4444444444', 'description': 'Mint flavoured floss for teeth.',
         'quantity': 25000},
        {'name': 'Paper Towels', 'sku': '5555555555',
         'description': 'Standard brown paper towels. Made from recycled materials.',
         'quantity': 5000},
        {'name': 'Toilet Paper', 'sku': '6666666666', 'description': 'White and soft two-ply toilet paper.',
         'quantity': 100000},
        {'name': 'Body Wash', 'sku': '7777777777', 'description': 'Natural soap for the human body.',
         'quantity': 800},
        {'name': 'Shampoo', 'sku': '8888888888', 'description': 'Silky smooth and fragrant soap for the hair.',
         'quantity': 32000},
        {'name': 'Tissue Paper', 'sku': '9999999999',
         'description': 'Softy and smooth white two-ply kleenex for the face',
         'quantity': 12000},
        {'name': 'Hand Mop', 'sku': '0000000000',
         'description': 'Standard gray hand mop for cleaning of wooden floors. Bucket not included.',
         'quantity': 50},
    ]
    for product in products_to_create:
        Product.objects.create(**product)


def reverse(apps, schema_editor):
    Product = apps.get_model('inventory', 'Product')
    Product.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('inventory', '0004_alter_product_shipment'),
    ]

    operations = [
        migrations.RunPython(forward, reverse_code=reverse)
    ]

# Generated by Django 3.2.13 on 2022-05-13 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sku', models.IntegerField(max_length=12, unique=True)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'inventory_products',
            },
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'inventory_shipments',
            },
        ),
    ]

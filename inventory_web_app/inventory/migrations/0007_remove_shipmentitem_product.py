# Generated by Django 3.2.13 on 2022-05-14 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20220513_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipmentitem',
            name='product',
        ),
    ]
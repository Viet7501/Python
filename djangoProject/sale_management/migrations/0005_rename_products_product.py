# Generated by Django 4.0.3 on 2022-04-08 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale_management', '0004_order_products_orderdetail'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale_management', '0003_remove_product_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]

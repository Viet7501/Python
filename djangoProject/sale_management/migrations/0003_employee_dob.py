# Generated by Django 4.0.3 on 2022-04-08 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale_management', '0002_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]

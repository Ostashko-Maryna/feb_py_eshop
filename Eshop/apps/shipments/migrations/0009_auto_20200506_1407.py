# Generated by Django 2.2.12 on 2020-05-06 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0008_auto_20200502_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='shipment_adress_apartment',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]

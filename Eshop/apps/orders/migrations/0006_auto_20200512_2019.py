# Generated by Django 2.2.12 on 2020-05-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200507_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_payment',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Portmone', 'Portmone')], default='Cash', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_shipment',
            field=models.CharField(choices=[('Pickup', 'Pickup'), ('New Post', 'New Post')], default='Pickup', max_length=100),
        ),
    ]

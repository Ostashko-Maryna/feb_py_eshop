# Generated by Django 2.2.4 on 2020-04-08 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_payment',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Portmone', 'Portmone')], default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_shipment',
            field=models.CharField(choices=[('Pickup', 'Pickup'), ('New Post', 'New Post')], default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('New order', 'New order'), ('Order processing', 'Order processing'), ('Packing', 'Packing'), ('Finished', 'Finished')], default='New order', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.UUIDField(default=uuid.UUID('9f9d5928-0551-4a88-bd8e-f2d660e9c7fc')),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_of_products', models.PositiveSmallIntegerField(default=1)),
                ('discont', models.PositiveSmallIntegerField(default=0)),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='orders.Order')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='products.Product')),
            ],
        ),
    ]
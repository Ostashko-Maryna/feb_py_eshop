<<<<<<< HEAD
# Generated by Django 2.2.12 on 2020-05-07 06:42
=======
# Generated by Django 2.2.12 on 2020-04-18 12:50
>>>>>>> b51214a3d1da53e51895592b76bea9584629e638

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ('orders', '0002_auto_20200416_1659'),
=======
        ('orders', '0002_auto_20200417_2223'),
>>>>>>> b51214a3d1da53e51895592b76bea9584629e638
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

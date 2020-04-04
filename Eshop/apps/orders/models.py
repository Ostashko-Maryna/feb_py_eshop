from django.db import models
from apps.products.models import Product

class Order(models.Model):
    order_number = models.PositiveSmallIntegerField(default=1, unique=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status_list = [
        ('Нове замовлення', 'Нове замовлення'),
        ('Обробляеться менеджером','Обробляеться менеджером'),
        ('Комплектуэться','Комплектуэться'),
        ('Виконано','Виконано'),
    ]
    order_status = models.CharField(max_length=100, default='Нове замовлення', choices=status_list)
    payment_list = [
        ('Готівка', 'Готівка'),
        ('Portmone', 'Portmone'),
    ]
    order_payment = models.CharField(max_length=100, blank=False, choices=payment_list)
    shipment_list = [
        ('Самовивіз', 'Самовивіз'),
        ('Нова почта', 'Нова почта'),
    ]
    order_shipment = models.CharField(max_length=100, blank=False, choices=shipment_list)
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    product = models.ManyToManyField(Product, db_table='OrderItem')
    amount_of_products =  models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.order_number

class User(models.Model):
    pass
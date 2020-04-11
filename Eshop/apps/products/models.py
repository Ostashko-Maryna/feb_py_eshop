from django.db import models
from django.utils.timezone import now


class Description(models.Model):#FIXME: rename to Kit
    description = models.TextField(max_length=5000, blank=True, verbose_name='Опис')
    characteristics = models.CharField(max_length=500, blank=True, verbose_name='Характеристики')
    available = models.BooleanField(default=True, verbose_name='Доступно')
    created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='created_product',
                                   verbose_name='Створено користувачем')
    # updated_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='updated_product',
    #                                verbose_name='Оновлено користувачем')
    created = models.DateTimeField(default=now, verbose_name='Створено')
    updated = models.DateTimeField(auto_now=True, verbose_name='Оновлено')

    def __str__(self):
        return '{} {}'.format(self.name, self.price)


class Review(models.Model):
    product_sn = models.ForeignKey(Product, default=0, on_delete=models.SET_NULL, null=True, related_name='product_sn',
                                   verbose_name='Відгук')
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='reviewer',
                             verbose_name='Користувач')
    review = models.TextField(max_length=5000, verbose_name='Відгук')
    available = models.BooleanField(default=True, verbose_name='Доступно')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')


# temporarily until the 'Galleries' model
class Galleries(models.Model):
    pass


class Product(models.Model):
    # django resists !!!???
    vendor_code = models.CharField(max_length=15, default='', verbose_name='Артикул')
    # Will we need a field (column) Category here?
    # category = models.ForeignKey('catalog.Category', on_delete=models.CASCADE, related_name='products', verbose_name='Категорія')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Назва')
    price = models.FloatField(default=0, verbose_name='Ціна')
    stock_count = models.PositiveIntegerField(default=0, verbose_name='В наявності')
    description = models.TextField(max_length=5000, default='', verbose_name='Опис')

    # django resists !!!???
    # review = models.ForeignKey(Review, on_delete=models.SET(False), blank=True, related_name='products', verbose_name='Відгук')
    available = models.BooleanField(default=True, verbose_name='Доступно')
    # django resists !!!???
    # created = models.DateTimeField(auto_now_add=True, default=timezone.now(), verbose_name='Створено')
    # created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated = models.DateTimeField(auto_now=True, verbose_name='Оновлено')


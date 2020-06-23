from django.db import models
# from django.utils.timezone import now


class Product(models.Model):
    vendor_code = models.CharField(max_length=15, default='', db_index=True, verbose_name='Артикул')
    # category = models.ForeignKey('catalog.Category', on_delete=models.CASCADE, related_name='products',
    #                              verbose_name='Категорія')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Назва')
    price = models.FloatField(default=0.0, verbose_name='Ціна') 
    stock_count = models.PositiveIntegerField(default=0, verbose_name='В наявності')
    description = models.TextField(max_length=5000, default='', verbose_name='Опис')
    characteristics = models.CharField(max_length=500, blank=True, verbose_name='Характеристики')
    available = models.BooleanField(default=True, verbose_name='Доступно')
    created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='created_product',
                                   verbose_name='Створено користувачем')
    # updated_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='updated_product',
    #                                verbose_name='Оновлено користувачем')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Оновлено')

    # @property
    # def quantity_left(self):
    #     if self.stock_count <= 0:
    #         raise ValueError('Unavailable product {}, {} (stock_count={})'.format(self.id, self.vendor_code,
    #                                                                               self.stock_count))
    #     return self.stock_count - sum([ci.quantity for ci in self.cartitem_set.all()])

    @property
    def quantity_left(self):
        if self.stock_count <= 0:
            self.available = False
            return 0
        else:
            self.available = True
            return self.stock_count

    def check_add_cart_item(self, desired_quantity):
        if self.quantity_left - desired_quantity < 0:
            raise ValueError('Unavailable product {}, {} (stock_count={})'.format(self.id, self.vendor_code,
                                                                                  self.stock_count))
            # or use False instead raise
            # return False
        return True

    def permissions(self, user):
        if self.created_by == user:
            # # if objects has property class Status (example Payments)
            # if self.status == Status.submitted:
            if self.available:
                return ['can_delete', 'can_edit', 'can_create']
            else:
                return ['can_create']
        else:
            return []

    def __str__(self):
        return '{} {}'.format(self.name, self.price)


class Review(models.Model):
    product = models.ForeignKey(Product, default=0, on_delete=models.SET_NULL, null=True,
                                related_name='reviews', verbose_name='Продукт')
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='reviews',
                             verbose_name='Користувач')
    review = models.TextField(max_length=5000, verbose_name='Відгук')
    available = models.BooleanField(default=True, verbose_name='Доступно')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')


class Kit(models.Model):
    products = models.ManyToManyField(Product, related_name='kits', verbose_name='Продукти')
    description = models.TextField(max_length=5000, verbose_name='Опис')
    available = models.BooleanField(default=True, verbose_name='Доступно')
    term = models.DateTimeField(blank=True, verbose_name='Термін до')
    created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='created_kit',
                                   verbose_name='Створено користувачем')
    # updated_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='updated_kit',
    #                                verbose_name='Оновлено користувачем')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Оновлено')

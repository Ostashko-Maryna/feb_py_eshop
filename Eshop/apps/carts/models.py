from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Cart(models.Model):
    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE, 
                                 null=True, blank=True,
                                 verbose_name='Власник')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated = models.DateTimeField(auto_now=True, verbose_name='Змінено')
    
    def __str__(self):
        return self.customer.username
    
    @property
    def not_empty(self):
        return self.cartitem_set.exists()
    not_empty.fget.short_description = 'Статус кошика'
    
    @property
    def total_price(self):
        return sum([ci.product.price*ci.quantity 
                    for ci in self.cartitem_set.all() if ci.cart_item_status == 'Доступно'])
    total_price.fget.short_description = 'Загальна вартість'
    
    @property
    def cart_list(self):
        return ['Назва товару: {} Ціна за одиницю: {} Кількість: {}'
                .format(ci.product.name, ci.product.price, ci.quantity)
                for ci in self.cartitem_set.all()
                if ci.cart_item_status == 'Доступно']
    cart_list.fget.short_description = 'Кошик'
    
    @property
    def not_available(self):
        return ['{} {}'.format(ci.product.name, ci.cart_item_status) 
                for ci in self.cartitem_set.all() 
                if ci.cart_item_status == 'Не доступно' 
                or ci.cart_item_status == 'Недостатня кількість']
    not_available.fget.short_description = 'Недоступні товари у кошику'
    
        
class CartItem(models.Model):
    product = models.ForeignKey('products.Product', 
                                on_delete=models.SET_NULL, 
                                null=True, blank=True,
                                verbose_name = 'Назва продукту',
                                related_name='cartitem',)
    cart = models.ForeignKey('carts.Cart', on_delete=models.CASCADE, 
                             verbose_name='Власник кошика',)
    customer = models.ForeignKey('auth.User', 
                                 on_delete=models.CASCADE, 
                                 null=True, blank=True,
                                 verbose_name = 'Власник',)
    quantity = models.PositiveSmallIntegerField(default=1, 
                                                verbose_name='Кількість')

    def clean(self):
        if self.quantity > self.product.stock_count:
            raise ValidationError(_('Доступно: %(value)s'),
            params={'value': self.product.stock_count},)
        elif self.quantity < 1:
            raise ValidationError(_('Не менше %(value)s'),
            params={'value': 1},)
    
    @property
    def product_name(self):
        return self.product.name
    
    @property
    def counter(self):
        self.product.stock_count -= self.quantity
        return self.product.stock_count
    
    @property
    def stock_count(self):
        return self.product.stock_count
    stock_count.fget.short_description = 'Доступно на складі'
               
    @property
    def cart_item_status(self):               
        if self.product.available == True and self.quantity <= self.product.stock_count:
            return 'Доступно'
        elif self.product.available == True and self.quantity > self.product.stock_count:
            return 'Недостатня кількість'
        else:
            return 'Не доступно'
    cart_item_status.fget.short_description = 'Статус товару'
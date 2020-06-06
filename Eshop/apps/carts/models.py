from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from apps_generic.whodidit.models import WhoDidIt
import uuid


class Cart(WhoDidIt):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT, 
                                 null=True, blank=True,
                                 verbose_name='Власник')
    def generator():
        return str(uuid.uuid4())
    cart_number = models.CharField(max_length=37, 
                                   default=generator, 
                                   editable=True,
                                   verbose_name='Номер кошика')
    
    def __str__(self):
        return self.cart_number
    
    @property    
    def cart_user_name(self):
        return self.user.username
    cart_user_name.fget.short_description = 'Власник кошика'
    
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
    
        
class CartItem(WhoDidIt):
    product = models.ForeignKey('products.Product', 
                                on_delete=models.SET_NULL, 
                                null=True, blank=True,
                                verbose_name = 'Назва продукту',
                                related_name='cartitem',)
    cart = models.ForeignKey('carts.Cart', on_delete=models.CASCADE, 
                             verbose_name='Номер кошика',)
    user = models.ForeignKey('auth.User', 
                                 on_delete=models.PROTECT, 
                                 null=True, blank=True,
                                 verbose_name = 'Власник',)
    quantity = models.PositiveSmallIntegerField(default=1, 
                                                verbose_name='Кількість')

    @property    
    def cart_user_name(self):
        return self.user
    cart_user_name.fget.short_description = 'Власник кошика'
    
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
    product_name.fget.short_description = 'Назва товару'
    
    @property
    def counter(self):
        self.product.stock_count -= self.quantity
        return self.product.stock_count
    counter.fget.short_description = 'Залишилось на складі'
     
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
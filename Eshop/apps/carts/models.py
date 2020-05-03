from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                                 null=True, blank=True,
                                 verbose_name='Власник')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated = models.DateTimeField(auto_now=True, verbose_name='Змінено')
    
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
                for ci in self.cartitem_set.all() if ci.cart_item_status == 'Доступно'] 
    cart_list.fget.short_description = 'Кошик'
    
    @property
    def not_available(self):
        return [ci.product.name for ci in self.cartitem_set.all() 
                if ci.cart_item_status == 'Не доступно' 
                or ci.cart_item_status == 'Недостатня кількість']
    not_available.fget.short_description = 'Недоступні товари у кошику'
    
        
class CartItem(models.Model):
    product = models.ForeignKey('products.Product', 
                                on_delete=models.SET_NULL, 
                                null=True, blank=True,
                                verbose_name = 'Назва продукту')    
    cart = models.ForeignKey('carts.Cart', on_delete=models.CASCADE, 
                             verbose_name='Кошик №',)
    user = models.ForeignKey(User, 
                                 on_delete=models.CASCADE, 
                                 null=True, blank=True,
                                 verbose_name = 'Власник',
                                 related_name='user')
    
    # @property
    # def field(self):
    #     return self.product.stock_count
    
    quantity = models.PositiveSmallIntegerField(default=1,
                            validators=[
                            MinValueValidator(1, 'Min value: 1'),
                            MaxValueValidator(100, 'Max value: {}'.format(100),)
                            ], 
                            verbose_name='Кількість')
    @property
    def cart_item_status(self):               
        if self.product.available == True and self.quantity <= self.product.stock_count:
            return 'Доступно'
        elif self.product.available == True and self.quantity > self.product.stock_count:
            return 'Недостатня кількість'
        else:
            return 'Не доступно'
    cart_item_status.fget.short_description = 'Статус товару'
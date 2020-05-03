from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


class Cart(models.Model):
    active = models.BooleanField(default=True) # cart not empty
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    @property
    def total_price(self):
        return sum([ci.product.price*ci.quantity for ci in self.cartitem_set.all()])

        
class CartItem(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True, blank=True, related_name=)
    quantity = models.IntegerField(default=1)       
    price = models.FloatField(blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

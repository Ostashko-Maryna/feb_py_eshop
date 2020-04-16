from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Cart(models.Model):
    active = models.BooleanField(default=True) # cart not empty
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
        
        
class CartItem(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1)       
    price = models.FloatField(blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
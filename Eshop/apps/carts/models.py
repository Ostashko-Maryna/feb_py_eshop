from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from apps.products.models import Product

class Cart(models.Model):
    active = models.BooleanField(default=True) # cart not empty
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    

class CartItem(models.Model):
    product_in = models.ManyToManyField(Product, blank=True)
    quantity = models.IntegerField(default=1)
    price_total = models.FloatField(blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    

    

# class Discount(Cart, discount):
#     Cart.total = Cart.total - Cart.total * discount
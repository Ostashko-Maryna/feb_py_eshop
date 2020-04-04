from django.db import models
from django.contrib.auth.models import User
#from ... import Product

class Cart(model.Model):
    customer = model.ForeignKey(User, blank=True)
    products = models.ManyToManyField(Product, blank=True)
    total = models.FloatField(default=0.00, max_digits=100)
    
class Discount(Cart, discount):
    Cart.total = Cart.total - Cart.total * discount
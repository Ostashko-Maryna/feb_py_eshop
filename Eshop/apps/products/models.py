from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200) 
    price = models.FloatField(default=0)
       
    def __str__(self):
        return '{} {}'.format(self.name, self.price)

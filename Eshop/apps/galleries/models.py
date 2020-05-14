import os

from django.conf import settings
from django.db import models


DEFAULT_PRODUCT_URL = (settings.STATIC_URL +'pictures/' + 'no_product.png')


class Gallery(models.Model):
    product = models.ForeignKey('products.Product', default=1, related_name='images', on_delete=models.PROTECT)
    image = models.ImageField(null=True, blank=True, upload_to="product_photos/%Y/%m/%d")
    name = models.CharField(max_length=100)
    
    class Size:
        min_size = 'min'
        max_size = 'max'
        mid_size = 'middle'

        min_x = 50
        min_y = 50
        max_x = 250
        max_y = 250
        mid_x = 150
        mid_y = 150

    size_list = [
        (Size.min_size, 'min'),
        (Size.max_size, 'max'),
        (Size.mid_size, 'middle'),
    ]

    size = models.CharField(max_length=100, default=Size.mid_size, choices=size_list)
    size_x = models.IntegerField(default=Size.mid_x)
    size_y = models.IntegerField(default=Size.mid_y)

    @property
    def image_url(self):
        try:
            # check file exist
            self.image.file
        except FileNotFoundError:
            return DEFAULT_PRODUCT_URL
        return self.image.url
    
    def __str__(self):
        return "{}".format(self.name)

    def save(self, *args, **kwargs):
        if self.size == 'min':
            self.size_x = self.Size.min_x
            self.size_y = self.Size.min_y
        elif self.size == 'max':
            self.size_x = self.Size.max_x
            self.size_y = self.Size.max_y

        super().save(*args, **kwargs)

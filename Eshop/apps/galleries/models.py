from django.db import models


class Gallery(models.Model):
    product = models.ForeignKey('products.Product', default=None, related_name='images', on_delete=models.PROTECT)
    image = models.ImageField(null=True, blank=True, upload_to="product_photos/%Y/%m/%d")
    name = models.CharField(max_length=100)
    
    class Size:
    	min_size = 'min'
    	max_size = 'max'
    	mid_size = 'middle'

    size_list = [
    	(Size.min_size, 'min'),
    	(Size.max_size, 'max'),
    	(Size.mid_size, 'middle'),
    ]

    size = models.CharField(max_length=100, default=Size.mid_size, choices=size_list)
    size_x = models.IntegerField(null=True)
    size_y = models.IntegerField(null=True)

    def __str__(self):
        return "{} {}".format(self.product, self.name)


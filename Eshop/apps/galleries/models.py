from django.db import models


class Gallery(models.Model):
    product = models.ForeignKey('products.Product', default=None, related_name='images', on_delete=models.PROTECT)
    image = models.ImageField(null=True, blank=True, upload_to="")
    name = models.CharField(max_length=100)
    
    class Size:
    	pass

    def __str__(self):
        return "{} {}".format(self.product, self.name)





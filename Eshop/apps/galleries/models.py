import os

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust, ResizeToFill

from django.conf import settings
from django.db import models

from apps_generic.whodidit.models import WhoDidIt


class Gallery(WhoDidIt):

    product = models.ForeignKey('products.Product', default=1, related_name='images', on_delete=models.PROTECT)
    image = models.ImageField(null=True, blank=True, upload_to="originals/%Y/%m/%d")
    name = models.CharField(max_length=100)

    image_small =ImageSpecField([ResizeToFill(50, 50)], source='image',  format='JPEG')
    image_medium =ImageSpecField([ResizeToFill(300, 200)], source='image',  format='JPEG')
    image_big =ImageSpecField([ResizeToFill(640, 480)], source='image',  format='JPEG')
    
    
    def _get_image_url(self, img):
        if img:
            return img.url
        return settings.DEFAULT_PRODUCT_URL

    @property
    def imageSmall_url(self):
        return self._get_image_url(self.image_small)

    @property
    def imageMedium_url(self):
        return self._get_image_url(self.image_medium)

    @property
    def imageBig_url(self):
        return self._get_image_url(self.image_big)

    def __str__(self):
        return "{}".format(self.name)


from django.contrib.auth.models import User 
from rest_framework import serializers

from apps.galleries.models import Gallery
from apps.products.models import Product


class ProductInGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id',  'name']


class GallerySerializer(serializers.ModelSerializer):
    product = ProductInGallerySerializer(read_only = True)

    image = serializers.ImageField(write_only=True)
    url = serializers.CharField(source='image_url', read_only=True)
    size_x = serializers.IntegerField(read_only=True)
    size_y = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Gallery
        fields = ['product', 'id', 'name', 'image', 'url', 'size', 'size_x', 'size_y']

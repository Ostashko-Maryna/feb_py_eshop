from django.contrib.auth.models import User 
from rest_framework import serializers

from apps.galleries.models import Gallery
from apps.products.models import Product


class ProductInGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id',  'name']


class GallerySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True)
    imageSmall_url = serializers.CharField(read_only=True)
    imageMedium_url = serializers.CharField(read_only=True)
    imageBig_url = serializers.CharField(read_only=True)
    
    class Meta:
        model = Gallery
        fields = ['product', 'id', 'name', 'image', 'imageSmall_url', 'imageMedium_url', 'imageBig_url']


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['product'] = ProductInGallerySerializer(
            Product.objects.get(pk=data['product'])).data
        return data


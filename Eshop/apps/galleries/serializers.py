from django.contrib.auth.models import User	
from rest_framework import serializers
from apps.galleries.models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True)
    url = serializers.CharField(source='image_url', read_only=True)
    size_x = serializers.IntegerField(read_only=True)
    size_y = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Gallery
        fields = ['id', 'product', 'name', 'image', 'url', 'size', 'size_x', 'size_y']

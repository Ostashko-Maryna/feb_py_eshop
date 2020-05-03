from django.contrib.auth.models import User	
from rest_framework import serializers
from apps.galleries.models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    #image = serializers.ImageField(write_only=True)
    #url = serializers.CharField(source='logo_url', read_only=True)
    
    class Meta:
        model = Gallery
        fields = ['id', 'product', 'name', 'image', 'size', 'size_x', 'size_y'] #url


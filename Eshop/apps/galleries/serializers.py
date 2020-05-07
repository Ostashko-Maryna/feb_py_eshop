from django.contrib.auth.models import User	
from rest_framework import serializers
from apps.galleries.models import Gallery


class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ['id', 'product', 'name', 'image', 'size', 'size_x', 'size_y']


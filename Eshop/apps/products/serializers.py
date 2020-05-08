from rest_framework import serializers
from .models import Product, Review, Kit


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'vendor_code', 'name', 'price', 'stock_count', 'quantity_left',
                  'description', 'characteristics', 'available', 'created_by', ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'review', 'available']


class KitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kit
        fields = ['id', 'products', 'description', 'available', 'term', 'created_by']
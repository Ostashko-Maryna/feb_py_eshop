from django.contrib.auth.models import User	
from rest_framework import serializers
from apps.carts.models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'active', 'customer', 'created', 'updated']
        
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product_in', 'quantity', 'price_total', 'cart']

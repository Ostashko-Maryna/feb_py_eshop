# from django.contrib.auth.models import User	
from rest_framework import serializers
from apps.carts.models import Cart, CartItem
from django.db.models import Sum


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'active', 'customer', 'created', 'updated', "total_price"]
        

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'price', 'cart']

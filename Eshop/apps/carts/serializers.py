# from django.contrib.auth.models import User	
from rest_framework import serializers
from apps.carts.models import Cart, CartItem
from django.db.models import Sum


class CartSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ['id', 'active', 'customer', 'created', 'updated', "total_price"]
        
    def get_total_price(self, total_price):
        # total_price = CartItem.objects.all().aggregate(total_price=Sum('Product.price'))
        total_price = CartItem.objects.aggregate(Sum('products.Product.price'))

        return total_price["total_price"]

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'price', 'cart']

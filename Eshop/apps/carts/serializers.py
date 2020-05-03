from rest_framework import serializers
from apps.carts.models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())    
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = CartItem
        fields = '__all__'
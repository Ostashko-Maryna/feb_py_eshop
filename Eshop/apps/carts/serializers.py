from rest_framework import serializers
from apps.carts.models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())    
    class Meta:
        model = Cart
        fields = ['id', 'customer', 'not_empty', 'created', 'updated', 
                  'total_price', 'cart_list', 'not_available']
        
        

class CartItemSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = CartItem
        fields = ['product', 'stock_count', 'quantity', 'cart', 'customer']
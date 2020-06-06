from rest_framework import serializers
from apps.carts.models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'
        
class CartItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CartItem
        # fields = '__all__'        
        fields = ['created_by',
                  'product', 
                  'stock_count', 
                  'quantity',
                  'cart']

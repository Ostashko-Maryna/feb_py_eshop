from rest_framework import serializers
from apps.carts.models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['id', 'user', 'not_empty', 'created_on', 'updated_on', 
                  'total_price', 'cart_list', 'not_available']
        
class CartItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CartItem
        fields = '__all__'        
        # fields = ['created_by',
        #           'product', 
        #           'stock_count', 
        #           'quantity',
        #           'cart']

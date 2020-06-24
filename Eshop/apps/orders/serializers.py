from rest_framework import serializers
from .models import Order, OrderItem

class OrderSerializer(serializers.ModelSerializer):
    #make all fields readonly
    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'user', 'order_date', 'order_cost',
            'order_payment', 'order_shipment', 'order_status',
        ]

    def create(self, *args, **kwargs):
        print('here!')
        #return Order.create_order(self.context['request'].user)
        return super().create(*args, **kwargs)

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'amount_of_products']

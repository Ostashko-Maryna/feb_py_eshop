from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Payments
from apps.orders.models import Order

class OrderInPaymentsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'order_status',
            'order_payment'
        ]

class PaymentsSerializer(serializers.ModelSerializer):
    order = OrderInPaymentsSerializer()
    permissions = serializers.SerializerMethodField()
    
    class Meta:
        model = Payments
        fields = [
            'id',
            'user',
            'order',
            'paymentsystem',
            'billAmount',
            'payment_date',
            'status',
            'permissions',
        ]

    def create(self, validated_data):
        order_data = validated_data.pop('order')
        created_payment = Payments.objects.create(**validated_data)
        order = Order.objects.get(id = order_data.get('id'))
        if order:
            created_payment.order = order
            created_payment.save()
        return created_payment

        # payment = super().create(validated_data)
        # order = Order.objects.filter(orders_data.get('id'))
        # if order:
            # updated_payment.order = order
            # updated_payment.save()
        # return updated_payment

    def update(self, instance, validated_data):
        order_data = validated_data.pop('order')
        updated_payment = super().update(instance, validated_data)
        order = Order.objects.get(id = order_data.get('id'))
        # order = Order.objects.filter(order_data.get('id'))
        if order:
            updated_payment.order = order
            updated_payment.save()
        return updated_payment

    def get_permissions(self, obj):
        return obj.permissions(self.context['request'].user)

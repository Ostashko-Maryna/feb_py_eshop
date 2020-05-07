from rest_framework import serializers
from apps.shipments.models import Shipment
from apps.orders.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['user','order_status', 'order_payment']

class ShipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipment
        fields = ['shipment_id', 'shipment_status_date_created']

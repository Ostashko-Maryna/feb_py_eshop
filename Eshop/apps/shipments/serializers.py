from rest_framework import serializers
from apps.shipments.models import Shipment
from apps.orders.models import Order


class OrderInShipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['user','order_status', 'order_payment']

class ShipmentSerializer(serializers.ModelSerializer):

	order = OrderInShipmentSerializer()

	class Meta:
		model = Shipment
		fields = ['shipment_id', 'shipment_status_date_created', 'order']

	def create(self, validated_data):
		orders_data = validated_data.pop('order')
		shipment = Shipment.objects.create(**validated_data)
		for order_data in orders_data:
			Order.objects.create(shipment=shipment, **order_data)
			return shipment
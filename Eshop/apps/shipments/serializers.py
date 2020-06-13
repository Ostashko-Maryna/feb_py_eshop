from rest_framework import serializers
from apps.shipments.models import Shipment
from apps.orders.models import Order

class OrderInShipmentSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField()

	class Meta:
		model = Order
		fields = ['id', 'user','order_status', 'order_payment']

class ShipmentSerializer(serializers.ModelSerializer):
	order = OrderInShipmentSerializer()
	permissions = serializers.SerializerMethodField()

	class Meta:
		model = Shipment
		fields = ['id',
					'shipment_id',
					'shipment_address_city',
					'shipment_status_date_created',
					'shipment_status_type',
					'permissions',
					'order']

	def get_permissions(self, obj):
		return obj.permissions(self.context['request'].user)
		
	def create(self, validated_data):
		orders_data = validated_data.pop('order')
		created_shipment = super().create(validated_data)
		order = Order.objects.filter(orders_data.get('id'))
		# TODO: cannot unpack non-iterable int object
		if order:
			created_shipment.order = order
			created_shipment.save()

	def update(self, instance, validated_data):
		orders_data = validated_data.pop('order')
		updated_shipment = super().update(instance, validated_data)
		order = Order.objects.filter(orders_data.get('id'))
		if order:
			updated_shipment.order = order
			updated_shipment.save()
		return updated_shipment

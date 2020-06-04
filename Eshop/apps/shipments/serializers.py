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

	class Meta:
		model = Shipment
		fields = ['id',
					'shipment_id',
					'shipment_address_city',
					'shipment_status_date_created',
					'order']

	def create(self, validated_data):
		orders_data = validated_data.pop('order')
		shipment = Shipment.objects.create(**validated_data)
		for order_data in orders_data:
			Order.objects.create(shipment=shipment, **order_data)
			return shipment

	def update(self, instance, validated_data):
		orders_data = validated_data.pop('order')
		updated_order = super().update(instance, validated_data)

		order = Order.objects.filter(orders_data.get('id'))
		if order:
			updated_order.order = order
			updated_order.save()
		return updated_order


# 	Errors:
	
# 	post >> IntegrityError at /shipments/
# null value in column "order_id" violates not-null constraint
# DETAIL:  Failing row contains (1, df, , , null, , null, Pick_up, 
# 	a098b81f-f8f2-4ae7-b16e-5d5ef69be4e3, 2020-06-04 04:52:03.554761+00, null, 2020-06-04 04:52:03.554724+00).

# 	put
# 	put >> TypeError at /shipments/3/
# cannot unpack non-iterable int object

	# def update(self, instance, validated_data):
	# 	orders_data = validated_data.pop('order')
	# 	orders = (instance.order).all()
	# 	orders = list(orders)
	# 	instance.shipment_address_city = validated_data.get('shipment_address_city',
	# 										instance.shipment_address_city)
	# 	instance.shipment_status_date_created = validated_data.get('shipment_status_date_created', 
	# 										instance.shipment_status_date_created)
	# 	instance.save()

	# 	for order_data in orders_data:
	# 		order = orders.pop(0)
	# 		order.user = order_data.get('user', order.user)
	# 		order.order_status = order_data.get('order_status', order.order_status)
	# 		order.order_payment = order_data.get('order_payment', order.order_payment)
	# 		order.save()
	# 	return instance
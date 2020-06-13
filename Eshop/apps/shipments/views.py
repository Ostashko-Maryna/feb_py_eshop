from django.shortcuts import get_object_or_404
from apps.orders.models import Order
from apps.shipments.models import Shipment
from apps.shipments.serializers import ShipmentSerializer, OrderInShipmentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from .filters import ShipmentsFilter
from .permissions import ShipmentPermission
from django.contrib.auth.models import User

class ShipmentList(generics.ListCreateAPIView):
	serializer_class = ShipmentSerializer
	pagination_class = LimitOffsetPagination
	filter_class = ShipmentsFilter
	permission_classes = [IsAuthenticated]
	
	def get_queryset(self):
		return Shipment.objects.filter(order__user=self.request.user)


class ShipmentDetails(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = ShipmentSerializer
	permission_classes = [IsAuthenticated, ShipmentPermission]


	def get_object(self):
		obj = get_object_or_404(Shipment, 
			pk=self.kwargs.get('shipment_id'),
			order__user=self.request.user)
		return obj


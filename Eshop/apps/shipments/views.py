from django.shortcuts import get_object_or_404
from apps.orders.models import Order
from apps.shipments.models import Shipment
from apps.shipments.serializers import ShipmentSerializer, OrderInShipmentSerializer
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

class ShipmentList(generics.ListCreateAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()
    pagination_class = LimitOffsetPagination

class ShipmentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShipmentSerializer

    def get_object(self):
        obj = get_object_or_404(Shipment, pk=self.kwargs.get('shipment_id'))
        return obj

class OrdersInShipmentList(generics.ListCreateAPIView):
    serializer_class = OrderInShipmentSerializer
    queryset = Order.objects.all()
    pagination_class = LimitOffsetPagination


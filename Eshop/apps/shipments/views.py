from django.shortcuts import get_object_or_404
from apps.orders.models import Order
from apps.shipments.models import Shipment
from apps.shipments.serializers import ShipmentSerializer, OrderInShipmentSerializer
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .filters import ShipmentsFilter, OrdersFilter

class ShipmentList(generics.ListCreateAPIView):
    serializer_class = ShipmentSerializer
    pagination_class = LimitOffsetPagination
    queryset = Shipment.objects.all()
    filter_class = ShipmentsFilter

class ShipmentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShipmentSerializer

    def get_object(self):
        obj = get_object_or_404(Shipment, pk=self.kwargs.get('shipment_id'))
        return obj

class OrdersInShipmentList(generics.ListCreateAPIView):
    serializer_class = OrderInShipmentSerializer
    queryset = Order.objects.all()
    filter_class = OrdersFilter
    pagination_class = LimitOffsetPagination


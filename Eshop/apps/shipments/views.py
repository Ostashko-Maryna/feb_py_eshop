from django.shortcuts import get_object_or_404
from apps.orders.models import Order
from apps.shipments.models import Shipment
from apps.shipments.serializers import ShipmentSerializer, OrderSerializer
from rest_framework import generics, filters

class ShipmentList(generics.ListCreateAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()

class ShipmentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_object(self):
        obj = get_object_or_404(Order, pk=self.kwargs.get('shipment_id'))
        return obj

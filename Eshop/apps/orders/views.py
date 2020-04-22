from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
from django.shortcuts import get_object_or_404
from rest_framework import generics

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer

    def get_object(self):
        obj = get_object_or_404(Order, pk=self.kwargs.get('order_id'))
        return obj

class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer

    def get_object(self):
        obj = get_object_or_404(OrderItem, pk=self.kwargs.get('orderitem_id'))
        return obj




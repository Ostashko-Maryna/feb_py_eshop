from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
from django.shortcuts import get_object_or_404
from rest_framework import generics, pagination
from .filters import OrderFilter
from .permisions import OrderPermisions, OrderItemPermisions #OrderListPermisions
from django.contrib.auth.models import User

class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 10
    pagination_class.max_limit = 100
    filter_class = OrderFilter
    #permission_classes = [OrderListPermisions]

    def get_queryset(self):
        user = self.request.user
        return user.order.all()

class OrderDetail(generics.RetrieveUpdateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [OrderPermisions]

    def get_object(self):
        obj = get_object_or_404(Order, pk=self.kwargs.get('order_id'))
        return obj

class OrderItemList(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 10
    pagination_class.max_limit = 100

    def get_queryset(self):
        order = get_object_or_404(Order, pk=self.kwargs.get('order_id'), user=self.request.user)
        return order.orderitem.all()

class OrderItemDetail(generics.RetrieveAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [OrderItemPermisions]

    def get_object(self):
        obj = get_object_or_404(OrderItem, pk=self.kwargs.get('orderitem_id'))
        return obj




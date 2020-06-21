from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.shortcuts import get_object_or_404
from apps.orders.models import Order, OrderItem
'''
class OrderListPermisions(BasePermission):
    def has_permission(self, request, view):
        return Order.user == view.request.user
'''
class OrderPermisions(BasePermission):
    def has_object_permission(self, request, view, obj):
        obj = get_object_or_404(Order, pk=view.kwargs.get('order_id'), user=view.request.user)
        if obj.order_status == Order.Status.new:
            return True
        return request.method in SAFE_METHODS

class OrderItemPermisions(BasePermission):
    def has_object_permission(self, request, view, obj):
        return get_object_or_404(OrderItem, pk=view.kwargs.get('orderitem_id'), order__user=view.request.user)
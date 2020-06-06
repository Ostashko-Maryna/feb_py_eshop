from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user 


class CartPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        return get_object_or_404(Cart,
                                pk=view.kwargs.get('cart_id'),
                                user=view.request.user.id,
                                )

class CartItemPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        return get_object_or_404(CartItem,
                                pk=view.kwargs.get('user_id'),
                                user=view.request.user.id,
                                )

# class AddCartItemPermission(BasePermission):
#     def has_permission(self, request, view):
#         if request.method == 'POST':
#             cartitem = get_object_or_404(CartItem, 
#                                      # pk=view.kwargs.get('cartitem_id'),
#                                      user=view.request.user,
#                                      )
#             return caritemt

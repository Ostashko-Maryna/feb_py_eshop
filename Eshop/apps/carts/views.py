from django.http import HttpResponse
from apps.carts.models import Cart, CartItem
from rest_framework import generics, pagination
from django.shortcuts import get_object_or_404
from apps.carts.serializers import CartSerializer, CartItemSerializer
from apps.carts.permissions import IsOwnerOrReadOnly, CartPermissions, CartItemPermissions
from apps.carts.filters import CartFilter, CartItemFilter
from rest_framework.response import Response


class CartList(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_class = CartFilter
    pagination_class.default_limit = 5
    pagination_class.max_limit = 25
    permission_classes = [IsOwnerOrReadOnly, CartPermissions, ]
    
    def get_queryset(self):
        return Cart.objects.filter(user_id=self.request.user.id)

    # def get_queryset(self):
    #     user = get_object_or_404('User', pk=self.kwargs.get('cart_id'))
    #     return user.cart.all()
    
    
class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 5
    pagination_class.max_limit = 25
    permission_classes = [IsOwnerOrReadOnly, CartPermissions, ]
    def get_object(self):
        obj = get_object_or_404(Cart, 
                                pk=self.kwargs.get('cart_id'),
                                user=self.request.user,)
        return obj
    
class CartItemList(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_class = CartItemFilter
    pagination_class.default_limit = 5
    pagination_class.max_limit = 25
    permission_classes = [IsOwnerOrReadOnly, CartPermissions, ]
    
    def get_queryset(self):
        # return CartItem.objects.filter(user=self.request.user)
        cart = get_object_or_404(Cart, 
                                pk=self.kwargs.get('cart_id'),
                                user=self.request.user)
        return CartItem.objects.filter(user=self.request.user, cart=cart)
    
class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 5
    pagination_class.max_limit = 25
    permission_classes = [IsOwnerOrReadOnly, CartItemPermissions, ]
    
    def get_object(self):
        obj = get_object_or_404(CartItem, 
                                pk=self.kwargs.get('cartitem_id'),
                                user=self.request.user,)
        return obj

from django.http import HttpResponse
from apps.carts.models import Cart, CartItem
from rest_framework import generics
from django.shortcuts import get_object_or_404
from apps.carts.serializers import CartSerializer, CartItemSerializer


def index(request):
    cart_list = CartItem.objects.all()
    return HttpResponse(', '.join([c.CartItem for c in cart_list]))


class CartInfo(generics.ListCreateAPIView):
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer



class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_object(self):
        obj = get_object_or_404(CartDetail.queryset, pk=self.kwargs.get('cart_item_id'))
        return obj
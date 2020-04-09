from django.http import HttpResponse
# from django.http import Http404
from apps.carts.models import Cart, CartItem
from rest_framework import generics
from django.shortcuts import get_object_or_404
from apps.carts.serializers import CartSerializer, CartItemSerializer

def index(request):
    cart_list = CartItem.objects.all()
    return HttpResponse(', '.join([c.cart_text for c in cart_list]))


# def index_other(request):
#     return HttpResponse("It\'s cart.")


class CartInfo(generics.ListCreateAPIView):
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def post(self, *args, **kwargs):
        return HttpResponse("It\'s  your cart.")


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = CartItemSerializer

    def get_object(self):
        obj = get_object_or_404(CartItem, pk=self.kwargs.get('cart_item_id'))
        return obj
from django.http import HttpResponse
from apps.carts.models import Cart, CartItem
from rest_framework import generics
from django.shortcuts import get_object_or_404
from apps.carts.serializers import CartSerializer, CartItemSerializer
from apps.carts.permissions import IsOwnerOrReadOnly

def index(request):
    cart_list = CartItem.objects.all()
    return HttpResponse(', '.join([c.CartItem for c in cart_list]))

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_object(self):
        obj = get_object_or_404(CartDetail.queryset, pk=self.kwargs.get('pk'))
        return obj
    
class CartItemCreate(generics.CreateAPIView):

    serializer_class = CartItemSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    
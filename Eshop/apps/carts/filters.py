import django_filters
from django_filters.rest_framework import FilterSet
from .models import Cart, CartItem


class CartFilter(FilterSet):
    def customer_contains(self, qs, contains, value):
        return qs.filter(user__icontains=value)
    def created_contains(self, qs, contains, value):
        return qs.filter(created_on__icontains=value) 

    user = django_filters.filters.CharFilter(method='user_contains')
    created_on = django_filters.filters.CharFilter(method='created_on_contains')

    class Meta:
        model = Cart
        fields = ['id']

class CartItemFilter(FilterSet):
    def cart_contains(self, qs, contains, value):
        return qs.filter(cart__icontains=value)
    def customer_contains(self, qs, contains, value):
        return qs.filter(user__icontains=value)     

    cart = django_filters.filters.CharFilter(method='cart_contains')
    user = django_filters.filters.CharFilter(method='user_contains')
    
    class Meta:
        model = CartItem
        fields = ['id']
    


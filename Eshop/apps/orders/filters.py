from django_filters import filters
from django_filters.rest_framework import FilterSet
from django.db.models import Q
from apps.orders.models import Order
from django.contrib.auth.models import User
from django.db import models

class OrderFilter(FilterSet):
    order_cost = filters.RangeFilter(label='фівфів')
    order_date = filters.DateFromToRangeFilter()
    order_payment = filters.ChoiceFilter(choices=Order.payment_list)
    order_shipment = filters.ChoiceFilter(choices=Order.shipment_list)
    order_status = filters.MultipleChoiceFilter(choices=Order.status_list)

    def filter_search(self, qs, search, value):
        search_fields = Q(order_number__icontains=value) | Q(orderitem__product__name__icontains=value)
        result = qs.filter(search_fields).distinct()
        return result

    search = filters.CharFilter(method='filter_search')
    #qs = Order.objects.filter(user=?)

    class Meta:
        model = Order
        fields = ['id']


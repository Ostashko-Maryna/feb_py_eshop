import django_filters
from django_filters.rest_framework import FilterSet
from .models import Shipment
from apps.orders.models import Order


class ShipmentsFilter(FilterSet):

	def shipment_address_city_contains(self, qs, contains, value):
		return qs.filter(shipment_address_city__icontains=value)

	shipment_address_city = django_filters.CharFilter(method='shipment_address_city_contains')

class OrdersFilter(FilterSet):

	def order_status_contains(self, qs, contains, value):
		return qs.filter(order_status__icontains=value)

	order_status = django_filters.CharFilter(method='order_status_contains')
import django_filters
from django.db.models import Q
from django_filters.rest_framework import FilterSet
from .models import UserProfile, DeliveryAddress


class UserProfileFilter(FilterSet):

    def phone_number_contains(self, qs, contains, value):
        return qs.filter(phone_number__icontains=value)

    def date_of_birth_contains(self, qs, contains, value):
        return qs.filter(date_of_birth__icontains=value)

    def vip_status_contains(self, qs, contains, value):
        return qs.filter(vip_status__icontains=value)

    phone_number = django_filters.filters.NumberFilter(method='phone_number_contains')
    date_of_birth = django_filters.filters.DateFilter(method='date_of_birth_contains')
    vip_status = django_filters.filters.BooleanFilter(method='vip_status_contains')

    class Meta:
        model = UserProfile
        fields = ['id']


class DeliveryAddressFilter(FilterSet):

    def region_contains(self, qs, contains, value):
        return qs.filter(region__icontains=value)

    def city_contains(self, qs, contains, value):
        return qs.filter(city__icontains=value)

    def zip_code_contains(self, qs, contains, value):
        return qs.filter(zip_code__icontains=value)

    region = django_filters.filters.CharFilter(method='region_contains')
    city = django_filters.filters.CharFilter(method='city_contains')
    zip_code = django_filters.filters.CharFilter(method='zip_code_contains')

    class Meta:
        model = DeliveryAddress
        fields = ['id']

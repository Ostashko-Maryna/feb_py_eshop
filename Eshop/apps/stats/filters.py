import django_filters
from django.contrib.postgres.fields import JSONField
from django_filters.rest_framework import FilterSet
from .models import Stats


class StatsFilter(FilterSet):

    def user_contains(self, qs, contains, value):
        return qs.filter(user__username__icontains=value)

    def action_contains(self, qs, contains, value):
        return qs.filter(data__Action__icontains=value)

    def product_contains(self, qs, contains, value):
        return qs.filter(data__Product__icontains=value)

    user = django_filters.filters.CharFilter(method='user_contains')
    action = django_filters.filters.CharFilter(method='action_contains')
    product = django_filters.filters.CharFilter(method='product_contains')

    class Meta:
        model = Stats
        fields = ['id']
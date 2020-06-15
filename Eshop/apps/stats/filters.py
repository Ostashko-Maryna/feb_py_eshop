import django_filters
from django.contrib.postgres.fields import JSONField
from django_filters.rest_framework import FilterSet
from .models import Stats


class StatsFilter(FilterSet):

    def user_contains(self, qs, contains, value):
        return qs.filter(user__username__icontains=value)

    #def action_contains(self, qs, contains, value):
       # value =Stats.objects.filter(data__has_key='Action')
        #return qs.filter(data__contains=value)

    user = django_filters.filters.CharFilter(method='user_contains')
    action = django_filters.filters.CharFilter(field_name='data__Action')
    product = django_filters.filters.CharFilter(field_name='data__Product')

    class Meta:
        model = Stats
        fields = ['id']
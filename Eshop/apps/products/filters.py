import django_filters

from django_filters.rest_framework import FilterSet
from .models import Product, Review, Kit


class ProductFilter(FilterSet):
    def vendor_code_contains(self, qs, contains, value):
        return qs.filter(vendor_code__icontains=value)

    def name_contains(self, qs, contains, value):
        return qs.filter(name__icontains=value)

    def description_contains(self, qs, contains, value):
        return qs.filter(description__icontains=value)

    def characteristics_contains(self, qs, contains, value):
        return qs.filter(characteristics__icontains=value)

    vendor_code = django_filters.filters.CharFilter(method='vendor_code_contains')
    name = django_filters.filters.CharFilter(method='name_contains')
    description = django_filters.filters.CharFilter(method='description_contains')
    characteristics = django_filters.filters.CharFilter(method='characteristics_contains')

    class Meta:
        model = Product
        fields = ['id']


class ReviewFilter(FilterSet):
    def review_contains(self, qs, contains, value):
        return qs.filter(review__icontains=value)

    review = django_filters.filters.CharFilter(method='review_contains')

    class Meta:
        model = Review
        fields = ['id']


class KitFilter(FilterSet):
    def description_contains(self, qs, contains, value):
        return qs.filter(description__icontains=value)

    description = django_filters.filters.CharFilter(method='description_contains')

    class Meta:
        model = Kit
        fields = ['id']

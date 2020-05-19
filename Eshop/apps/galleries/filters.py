import django_filters

from django_filters.rest_framework import FilterSet
from .models import Gallery


class ProductGalleryFilter(FilterSet):

    def name_contains(self, qs, contains, value):
        return qs.filter(name__icontains=value)

    def size_contains(self, qs, contains, value):
        return qs.filter(size__icontains=value)

    name = django_filters.filters.CharFilter(method='name_contains')
    size = django_filters.filters.CharFilter(method='size_contains')

    class Meta:
        model = Gallery
        fields = ['id']


class GalleryFilter(ProductGalleryFilter):

    class Meta:
        model = Gallery
        fields = ['id', 'product']
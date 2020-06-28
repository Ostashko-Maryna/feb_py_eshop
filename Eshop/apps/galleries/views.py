# from django.shortcuts import render
# from django.http import Http404

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from apps.galleries.models import Gallery
from apps.products.models import Product
from apps.galleries.serializers import GallerySerializer
from .filters import GalleryFilter, ProductGalleryFilter
from .permissions import GalleryPermission


class GalleryList(generics.ListCreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    pagination_class = LimitOffsetPagination
    filter_class = GalleryFilter
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     print('HHH')
    #     print(self.request.query_params)
    #     if 'search' in self.request.query_params:
    #         search_name = self.request.query_params['search']
    #         return Gallery.objects.filter(name__icontains=search_name)
    #     return Gallery.objects.all()


class ProductGalleryList(generics.ListCreateAPIView):
    serializer_class = GallerySerializer
    pagination_class = LimitOffsetPagination
    filter_class = ProductGalleryFilter
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        product = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        #return Review.objects.filter(prduct_id=self.kwargs.get('product_id'))
        return product.images.all()


class GalleryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticated, GalleryPermission]

    def get_object(self):
        obj = get_object_or_404(Gallery, pk=self.kwargs.get('gallery_id'))
        return obj


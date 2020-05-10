# from django.shortcuts import render
# from django.http import Http404

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from rest_framework import generics
from apps.galleries.models import Gallery
from apps.products.models import Product
from apps.galleries.serializers import GallerySerializer


class GalleryList(generics.ListCreateAPIView):
	queryset = Gallery.objects.all()
	serializer_class = GallerySerializer


class ProductGalleryList(generics.ListCreateAPIView):
    serializer_class = GallerySerializer

    def get_queryset(self):
        product = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        #return Review.objects.filter(prduct_id=self.kwargs.get('product_id'))
        return product.images.all()


class GalleryDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = GallerySerializer

    def get_object(self):
        obj = get_object_or_404(Gallery, pk=self.kwargs.get('gallery_id'))
        return obj


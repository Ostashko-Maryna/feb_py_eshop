# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from .models import Product, Review, Kit
from .serializers import ProductSerializer, ReviewSerializer, KitSerializer
from .permissions import ProductPermission

from .filters import ProductFilter, ReviewFilter, KitFilter


# def index(request):
#     products = Product.objects.all()
#     output = ', '.join([str(c) for c in products])
#     return HttpResponse(output)
#
#
# def detail(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     return HttpResponse(product)


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    filter_class = ProductFilter
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    filter_class = ProductFilter

# Variants without permission_classes = [IsAuthenticated]
#     def get_queryset(self):
#         return Product.objects.filter(created_by=self.request.user)

    def get_queryset(self):
        if 'search' in self.request.query_params:
            search_name = self.request.query_params['search']
            return Product.objects.filter(name__icontains=search_name)
        return Product.objects.all()

# Variants without filter_class = ProductFilter
#     def get_queryset(self):
#         if 'search' in self.request.query_params:
#             search_name = self.request.query_params['search']
#             return Product.objects.filter(name__icontains=search_name)
#         return Product.objects.all()
#
#     def get_queryset(self, *args, **kwargs):
#         if self.request.GET.get('search'):
#             return Product.objects.filter(product_name__icontains=self.request.GET.get('search'))
#         return Product.objects.all()


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, ProductPermission]

    def get_object(self):
        obj = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        return obj


class ProductReviewsList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    filter_class = ReviewFilter
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        product = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        # return Review.objects.filter(prduct_id=self.kwargs.get('product_id'))
        return product.reviews.all()


class ProductKitsList(generics.ListAPIView):
    serializer_class = KitSerializer
    filter_class = KitFilter
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        product = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        return product.kits.all()


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_class = ReviewFilter
    pagination_class = LimitOffsetPagination


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer

    def get_object(self):
        obj = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return obj


class KitList(generics.ListCreateAPIView):
    queryset = Kit.objects.all()
    serializer_class = KitSerializer
    filter_class = KitFilter
    pagination_class = LimitOffsetPagination


class KitDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = KitSerializer

    def get_object(self):
        obj = get_object_or_404(Kit, pk=self.kwargs.get('kit_id'))
        return obj

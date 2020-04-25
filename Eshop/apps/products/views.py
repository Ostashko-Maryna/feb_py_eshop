from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product, Review, Kit
from rest_framework import generics
from .serializers import ProductSerializer, ReviewSerializer


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
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_object(self):
        obj = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        return obj


class ProductReviews(generics.ListAPIView):

    serializer_class = ReviewSerializer

    def get_queryset(self):
        product = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        #return Review.objects.filter(prduct_id=self.kwargs.get('product_id'))
        return product.reviews.all()


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer

    def get_object(self):
        obj = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return obj

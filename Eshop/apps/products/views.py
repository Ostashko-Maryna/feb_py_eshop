from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product, Review, Kit


def index(request):
    products = Product.objects.all()
    output = ', '.join([str(c) for c in products])
    return HttpResponse(output)


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return HttpResponse(product)

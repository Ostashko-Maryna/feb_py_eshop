from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from .models import Product, Review, Kit


# Variant uses HTTP 403 Forbidden
# class ProductPermission(BasePermission):
#     def has_permission(self, request, view):
#         return Product.objects.filter(
#             pk=view.kwargs.get('product_id'),
#             created_by=view.request.user
#         ).exists()

# Variant uses HTTP 404 Page not found
# class ProductPermission(BasePermission):
#     def has_permission(self, request, view):
#         return get_object_or_404(
#             Product,
#             pk=view.kwargs.get('product_id'),
#             created_by=view.request.user
#         )

# Variant uses HTTP 404 Page not found
# & if objects has available True
class ProductPermission(BasePermission):
    def has_permission(self, request, view):
        obj = get_object_or_404(
            Product,
            pk=view.kwargs.get('product_id'),
            created_by=view.request.user
        )
        if request.method != 'Get':
            # # if objects has property class Status (example Payments)
            # return obj.status == Status.submitted
            return obj.available == True
        return obj

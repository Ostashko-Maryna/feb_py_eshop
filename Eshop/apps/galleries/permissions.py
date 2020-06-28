from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from apps.galleries.models import Gallery


class GalleryPermission(BasePermission):
    def has_permission(self, request, view):
        return get_object_or_404(
            Gallery, 
            product_id=view.kwargs.get('product_id'), 
            pk=view.kwargs.get('gallery_id'),
        )


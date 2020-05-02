from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD or OPTIONS requests.
            return True
        return obj.customer == request.user # Instance must have an attribute named `customer`.
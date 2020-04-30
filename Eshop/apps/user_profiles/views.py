from django.http import HttpResponse
from django.http import Http404
from .models import UserProfile, DeliveryAddress

from rest_framework import generics
from .serializers import UserProfileSerializer, DeliveryAddressSerializer
from django.shortcuts import get_object_or_404
from .models import UserProfile, DeliveryAddress


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        obj = get_object_or_404(UserProfile, pk=self.kwargs.get('user_profile_id'))
        return obj


class DeliveryAddressList(generics.ListCreateAPIView):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressSerializer


class DeliveryAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeliveryAddressSerializer

    def get_object(self):
        obj = get_object_or_404(DeliveryAddress, pk=self.kwargs.get('delivery_address_id'))
        return obj

"""
def index(request):
    user_profile_list = UserProfile.objects.all()
    return HttpResponse("Hello, OTHER world. You're at the polls index.")

"""



from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile, DeliveryAddress


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['id', 'user','date_of_birth', 'phone_number', 'vip_status']


class DeliveryAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryAddress
        fields = ['id', 'user', 'region', 'city', 'street', 'house_number', 'apartment_number', 'zip_code']

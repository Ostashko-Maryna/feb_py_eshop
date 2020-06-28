from django.contrib import admin
from . models import UserProfile, DeliveryAddress


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'phone_number', 'vip_status']


admin.site.register(UserProfile, UserProfileAdmin)


class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'region', 'city', 'street', 'house_number', 'apartment_number', 'zip_code']


admin.site.register(DeliveryAddress, DeliveryAddressAdmin)

from django.urls import path

from . import views

urlpatterns = [
    path('user_profile/', views.UserProfileList.as_view(), name='list'),
    path('user_profile/<int:user_profile_id>/', views.UserProfileDetail.as_view(), name='details'),
    path('delivery_address/', views.DeliveryAddressList.as_view(), name='list'),
    path('delivery_address/<int:delivery_address_id>/', views.DeliveryAddressDetail.as_view(), name='details'),
]

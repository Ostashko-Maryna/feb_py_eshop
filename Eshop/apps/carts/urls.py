from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.CartInfo.as_view(), name='CartInfo'),
    path('cart/<int:cart_id>/', views.CartDetail.as_view(), name='CartDetail'),
]
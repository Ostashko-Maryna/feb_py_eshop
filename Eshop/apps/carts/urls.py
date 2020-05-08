from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/<int:pk>/', views.CartDetail.as_view(), name='CartDetail'),
    path('create/', views.CartItemCreate.as_view(), name='CartItemCreate'),
]
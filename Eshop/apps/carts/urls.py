from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('other/', views.index_other, name='index_other'),
    path('cart/', views.CartInfo.as_view(), name='CartInfo'),
    path('cart/<int:cart_id>/', views.CartDetail.as_view(), name='CartDetail'),
]
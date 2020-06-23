from django.urls import path

from . import views

urlpatterns = [
    path('', views.CartList.as_view(), name='CartList'),
    path('<int:cart_id>/', views.CartDetail.as_view(), name='CartDetail'),
    path('<int:cart_id>/cartitem/', views.CartItemList.as_view(), name='CartItemList'),
    path('<int:cart_id>/cartitem/<int:cartitem_id>/', views.CartItemDetail.as_view(), name='CartItemDetail'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>/cartlist/', views.CartList.as_view(), name='CartList'),
    path('<int:user_id>/<int:cart_id>/', views.CartDetail.as_view(), name='CartDetail'),
    path('<int:user_id>/create/', views.CartItemCreate.as_view(), name='CartItemCreate'),
    path('<int:user_id>/<int:cart_id>/cilist/', views.CartItemList.as_view(), name='CartItemList'),
    path('<int:user_id>/<int:cart_id>/<int:cartitem_id>/', views.CartItemDetail.as_view(), name='CartItemDetail'),
]
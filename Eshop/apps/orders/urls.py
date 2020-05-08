from django.urls import path
from . import views

urlpatterns = [
    path('user<int:user_id>/', views.OrderList.as_view(), name='orders'),
    path('<int:order_id>/', views.OrderDetail.as_view(), name='order'),
    path('<int:order_id>/orderitems/', views.OrderItemList.as_view(), name='orderitems'),
    path('orderitem<int:orderitem_id>', views.OrderItemDetail.as_view(), name='orderitem'),
]

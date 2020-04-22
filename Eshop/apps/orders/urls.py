from  django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderList.as_view(), name='orders'),
    path('<int:order_id>/', views.OrderDetail.as_view(), name='order'),
    path('orderitems/', views.OrderItemList.as_view(), name='orderitems'),
    path('orderitems/<int:orderitem_id>', views.OrderItemDetail.as_view(), name='orderitem'),
]

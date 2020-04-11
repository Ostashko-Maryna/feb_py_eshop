from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('notification/', views.NotificationList.as_view(), name='list'),
    path('notification/<int:notification_id>/', views.NotificationDetail.as_view(), name='details'),
]

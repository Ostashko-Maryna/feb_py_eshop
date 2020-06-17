from django.urls import path
from . import views

urlpatterns = [
    path('', views.StatsList.as_view(), name='list'),
    path('<int:statss_id>', views.StatsDetail.as_view(), name='detail')
]
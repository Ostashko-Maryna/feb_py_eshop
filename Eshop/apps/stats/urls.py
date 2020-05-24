from django.urls import path
from . import views

urlpatterns = [
    path('', views.StatsList.as_view(), name='list'),
    path('<int:stats_id>', views.StatsDetail.as_view(), name='detail')
]
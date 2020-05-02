from django.urls import path

from . import views

urlpatterns = [
	path('', views.GalleryList.as_view(), name='list'),
    path('<int:product_id>/', views.ProductGalleryList.as_view(), name='list'),
    path('<int:product_id>/<int:gallery_id>/', views.GalleryDetail.as_view(), name='details'),
]

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.ProductList.as_view(), name='list'),
    path('<int:product_id>/', views.ProductDetail.as_view(), name='detail'),
    path('<int:product_id>/reviews/', views.ProductReviewsList.as_view(), name='list_product_reviews'),
    path('<int:product_id>/kits/', views.ProductKitsList.as_view(), name='list_product_kits'),
    path('reviews/', views.ReviewList.as_view(), name='list'),
    path('reviews/<int:review_id>/', views.ReviewDetail.as_view(), name='detail'),
    path('kits/', views.KitList.as_view(), name='list'),
    path('kits/<int:kit_id>/', views.KitDetail.as_view(), name='detail'),

]

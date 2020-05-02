from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.ProductList.as_view(), name='list'),
    path('<int:product_id>/', views.ProductDetail.as_view(), name='detail'),
    path('<int:product_id>/reviews/', views.ProductReviews.as_view(), name='list_product_reviews'),
    path('reviews/', views.ReviewList.as_view(), name='list'),
    path('reviews/<int:review_id>/', views.ReviewDetail.as_view(), name='detail'),
]

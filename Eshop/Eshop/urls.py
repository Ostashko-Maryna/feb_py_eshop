from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('orders/', include('apps.orders.urls')),
	path('payments/', include('apps.payments.urls')),
    path('notifications/', include('apps.notifications.urls')),
    path('products/', include('apps.products.urls')),
    path('cart/', include('apps.carts.urls')),
    path('galleries/', include('apps.galleries.urls')),
    path('user_profiles/', include('apps.user_profiles.urls')),
    path('rest-auth/', include('rest_framework.urls')),
    path('shipments/', include('apps.shipments.urls')),
]

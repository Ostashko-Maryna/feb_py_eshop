from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('payments/', views.PaymentsList.as_view(), name = 'payments_list'),
	path('payments/<int:payment_id>/', 
		views.PaymentsDetail.as_view(), name = 'payments_detail'
	),
]

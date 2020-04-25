from django.urls import path
from . import views

urlpatterns = [
	path('', views.index_payments, name = 'index_payments'),
	path('payments/', views.PaymentsList.as_view(), name = 'payments_list'),
	path('payments/<int:payment_id>/', 
		views.PaymentsDetail.as_view(), name = 'payments_detail'
	),
	path('log/', views.index_paymentsystemlog, 
		name = 'index_paymentsystemlog'
	),
	path('paymentsystemlog/', views.PaymentSystemLogList.as_view(), 
		name = 'paymentsystemlog_list'
	),
	path('paymentsystemlog/<int:paymentsystemlog_id>/', 
		views.PaymentSystemLogDetail.as_view(), 
		name = 'paymentsystemlog_detail'
	),
]

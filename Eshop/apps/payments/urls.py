from django.urls import path
from . import views

urlpatterns = [
    path('', views.PaymentsList.as_view(), name = 'payments_list'),
    path('<int:payment_id>/', 
        views.PaymentsDetail.as_view(), name = 'payments_detail'
    ),
    # path('paymentsystemlog/', views.PaymentSystemLogList.as_view(), 
        # name = 'paymentsystemlog_list'
    # ),
    # path('paymentsystemlog/<int:paymentsystemlog_id>/', 
        # views.PaymentSystemLogDetail.as_view(), 
        # name = 'paymentsystemlog_detail'
    # ),
]

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Payments, PaymentSystemLog
from rest_framework import generics
from .serializers import PaymentsSerializer, PaymentSystemLogSerializer


def index_payments(request):
	payments_list = Payments.objects.all()
	return HttpResponse(payments_list)

def index_paymentsystemlog(request):
	paymentsystemlog_list = PaymentSystemLog.objects.all()
	return HttpResponse(paymentsystemlog_list)

class PaymentsList(generics.ListCreateAPIView):
	queryset = Payments.objects.all()
	payments_serializer = PaymentsSerializer

class PaymentsDetail(generics.RetrieveUpdateDestroyAPIView):
	payments_serializer = PaymentsSerializer

	def get_object(self):
		obj = get_object_or_404(Payments, pk=self.kwargs.get('payments_id'))
		return obj


class PaymentSystemLogList(generics.ListCreateAPIView):
	queryset = PaymentSystemLog.objects.all()
	paymentsystemlog_serializer = PaymentSystemLogSerializer

class PaymentSystemLogDetail(generics.RetrieveUpdateDestroyAPIView):
	paymentsystemlog_serializer = PaymentSystemLogSerializer

	def get_object(self):
		obj = get_object_or_404(PaymentSystemLog, 
			pk=self.kwargs.get('paymentsystemlog_id')
		)
		return obj

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Payments, PaymentSystemLog
from rest_framework import generics
from .serializers import PaymentsSerializer

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

class PaymentSystemLogDetail(generics.RetrieveUpdateDestroyAPIView):
	def get_object(self):
		obj = get_object_or_404(PaymentSystemLog, 
			pk=self.kwargs.get('paymentsystemlog_id')
		)
		return obj

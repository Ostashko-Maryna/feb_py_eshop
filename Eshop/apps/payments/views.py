from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Payments
from rest_framework import generics
from .serializers import PaymentsSerializer


def index(request):
	payments_list = Payments.objects.all()
	return HttpResponse(payments_list)

class PaymentsList(generics.ListCreateAPIView):
	queryset = Payments.objects.all()
	question_serializer = PaymentsSerializer

class PaymentsDetail(generics.RetrieveUpdateDestroyAPIView):
	question_serializer = PaymentsSerializer

	def get_object(self):
		obj = get_object_or_404(Payments, pk=self.kwargs.get('payments_id'))
		return obj

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Payments, PaymentSystemLog
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .serializers import PaymentsSerializer

class PaymentsList(generics.ListCreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    pagination_class = LimitOffsetPagination

class PaymentsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentsSerializer

    def get_object(self):
        obj = get_object_or_404(Payments, pk=self.kwargs.get('payment_id'))
        return obj


class PaymentSystemLogList(generics.ListCreateAPIView):
    queryset = PaymentSystemLog.objects.all()
    pagination_class = LimitOffsetPagination

class PaymentSystemLogDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_object(self):
        obj = get_object_or_404(PaymentSystemLog, 
            pk=self.kwargs.get('paymentsystemlog_id')
        )
        return obj

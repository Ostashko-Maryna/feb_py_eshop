from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Payments

class PaymentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payments
        fields = [
            'id',
            'user',
            'order',
            'paymentsystem',
            'billAmount',
            'payment_date',
            'status',
        ]

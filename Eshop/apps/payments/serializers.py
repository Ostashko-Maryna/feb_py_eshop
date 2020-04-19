from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Payments, PaymentSystemLog

class PaymentsSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Payments
		fields = [
			'id',
			'payment_date',
			'user',
			'order',
			'paysystem',
		]


class PaymentSystemLogSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = PaymentSystemLog
		fields = [
			'id',
			'order',
			'raw_data',
			'sent_at',	
			'raw_response',
			'processed_at',
			'processed_ok',
		]

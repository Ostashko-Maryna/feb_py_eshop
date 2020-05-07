from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Payments
from apps.orders.models import Order
import datetime

class PaymentsTestCase(TestCase):
	def setUp(self):
		user = User.objects.create()
		user.save()
		order = Order.objects.create(user_id = 0)
		order.save()
		p = Payments.objects.create(
			user = user,
			order = order,
			paymentsystem = 'portmone',
			billAmount = 100.0,
			payment_date = datetime.datetime.now(),
			status = 'completed',
		)
		self.c = APIClient()
	
	def test_payments(self):
		print()
		response = self.c.get('/payments/')
		self.assertEqual(response.status_code, 200)
		print(response.json())
		'''self.assertEqual(response.json(),[{
		
		}]'''
		

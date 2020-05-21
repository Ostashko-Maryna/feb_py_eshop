from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Payments
from apps.orders.models import Order
from datetime import date


class PaymentsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create()
        self.order = Order.objects.create()
        self.payment = Payments.objects.create(
            user = self.user,
            order = self.order,
            paymentsystem = 'portmone',
            billAmount = 100.0,
            payment_date = date.today(),
            status = 'completed',
        )
        self.client = APIClient()
    
    def test_payments_get(self):
        print()
        response = self.client.get('/payments/')
        self.assertEqual(response.status_code, 200)
        print(response.json())
        self.assertEqual(response.json(),[{
            'id': self.payment.id, 
            'payment_date': str(
                self.payment.payment_date.isoformat().replace('+00:00', 'Z')
            ), 
            'user': self.user.id, 
            'order': self.order.id, 
            'paymentsystem': str(self.payment.paymentsystem)
        }])
    
    def test_payments_post(self):
        request = self.client.post('/payments/',{
            'id': self.payment.id, 
            'payment_date': date.today(), 
            'user': self.user.id, 
            'order': self.order.id, 
            'paymentsystem': self.payment.paymentsystem
        })
        print(request)
        self.assertEqual(request.status_code, 201)

    def test_payments_detail(self):
        print()
        number =  self.payment.id
        response = self.client.get('/payments/{}/'.format(number))
        self.assertEqual(response.status_code, 200)
        print(response.json())
        self.assertEqual(response.json(),{
            'id': self.payment.id, 
            'payment_date': str(
                self.payment.payment_date.isoformat().replace('+00:00', 'Z')
            ), 
            'user': self.user.id, 
            'order': self.order.id, 
            'paymentsystem': str(self.payment.paymentsystem)
        })

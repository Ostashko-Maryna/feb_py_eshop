from django.test import TestCase
from rest_framework.test import APIClient
from apps.orders.models import Order, OrderItem

class OrdersTestAPI(TestCase):
    def setUp(self):
        #self.order = Order.objects.create()
        self.c = APIClient()

    def test_list(self):
        print()
        response = self.c.get('/orders/user1')
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.json(), )
        print(response.json())


#from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from apps.orders.models import Order, OrderItem
from django.contrib.auth.models import User
import uuid

class OrdersTestAPI(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('user_name', 'user_name@gmail.com', 'password')
        self.order = Order.objects.create(order_number=uuid.uuid4(), user=self.user)
        self.c = APIClient()

    def test_list(self):
        response = self.c.get('/orders/user1/')
        self.assertEqual(response.status_code, 200)
        '''
        self.assertEqual(response.json(), [{
            'id': self.order.id,
            'order_number': self.order.order_number,
            'order_date': now(),
            'order_status': self.order.order_status,
            'order_payment': self.order.order_payment,
            'order_shipment': self.order.order_shipment,
            'user': self.user.id,
            'order_cost': '0.00',
        }])
        '''

        self.assertEqual(response.json(), [{
            'id': self.order.id,
            'order_number': self.order.order_number,
            'order_date': self.order.order_date,
            'order_status': self.order.order_status,
            'order_payment': self.order.order_payment,
            'order_shipment': self.order.order_shipment,
            'user': self.order.user.id,
            'order_cost': self.order.order_cost,
        }])
        print(response.json())


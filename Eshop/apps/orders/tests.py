#from django.test import TestCase
from rest_framework.test import APIClient, APITestCase, RequestsClient
from apps.orders.models import Order, OrderItem
from django.contrib.auth.models import User
from apps.products.models import Product
from apps.user_profiles.models import UserProfile
import uuid
from django.db.models.deletion import ProtectedError

class OrdersTestAPI(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('user_name', 'user_name@gmail.com', 'password')
        self.product = Product.objects.create(name='test product', created_by=self.user)
        self.order = Order.objects.create(user=self.user)
        self.orderitem = self.order.orderitem.create(order=self.order, product=self.product)
        self.c = APIClient()
        self.c.login(username='user_name', password='password')
        self.maxDiff = None

    def test_get_order_list(self):
        print(self.user.id)
        print(self.user.userprofile.vip_status)
        print(self.order.id)
        print(self.order.order_status)
        print(self.orderitem.id)
        response = self.c.get('/orders/user{}/?limit=1'.format(self.user.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'count': len(response.json()['results']),
            'next': None,
            'previous': None,
            'results': [{
                'id': self.order.id,
                'order_number': self.order.order_number,
                'order_date': self.order.order_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                'order_status': self.order.order_status,
                'order_payment': self.order.order_payment,
                'order_shipment': self.order.order_shipment,
                'user': self.order.user.id,
                'order_cost': '0.00',
            }]
        })

    def test_get_orderitem_list(self):
        print(self.user.id)
        print(self.user.userprofile.id)
        print(self.order.id)
        print(self.orderitem.id)
        response = self.c.get('/orders/{}/orderitems/?limit=1'.format(self.order.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'count': len(response.json()['results']),
            'next': None,
            'previous': None,
            'results': [{
                'id': self.orderitem.id,
                'order': self.orderitem.order.id,
                'product': self.orderitem.product.id,
                'amount_of_products': self.orderitem.amount_of_products
            }]
        })

    def test_get_order(self):
        print(self.user.id)
        print(self.order.id)
        print(self.orderitem.id)
        response = self.c.get('/orders/{}/'.format(self.order.id))
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'id': self.order.id,
            'order_number': self.order.order_number,
            'order_date': self.order.order_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            'order_status': self.order.order_status,
            'order_payment': self.order.order_payment,
            'order_shipment': self.order.order_shipment,
            'user': self.order.user.id,
            'order_cost': '0.00',
        })

    def test_get_orderitem(self):
        print(self.user.id)
        print(self.order.id)
        print(self.orderitem.id)
        response = self.c.get('/orders/orderitem{}/'.format(self.orderitem.id))
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'id': self.orderitem.id,
            'order': self.orderitem.order.id,
            'product': self.orderitem.product.id,
            'amount_of_products': self.orderitem.amount_of_products
        })

    def test_post_order(self):
        print(self.user.id)
        print(self.order.id)
        print(self.orderitem.id)
        response = self.c.post(
            '/orders/user{}/'.format(self.user.id),data={
                'user': self.user.id
            }
        )
        print(response.json())
        self.assertEqual(response.status_code, 201)
        created_order = Order.objects.get(id=response.json()['id'])
        print(response.json()['id'])
        print(created_order.id)
        self.assertEqual(response.json(), {
            'id': created_order.id,
            'order_number': created_order.order_number,
            'order_date': created_order.order_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            'order_status': created_order.order_status,
            'order_payment': created_order.order_payment,
            'order_shipment': created_order.order_shipment,
            'user': created_order.user.id,
            'order_cost': str(created_order.order_cost),
        })

    def test_put_order(self):
        print(self.user.id)
        print(self.order.id)
        print(self.orderitem.id)
        print(self.order.order_number)
        response = self.c.put(
            '/orders/{}/'.format(self.order.id),
            data={
                'id': self.order.id,
                'order_number': str(uuid.uuid4())[:23],
                'order_date': self.order.order_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                'order_status': self.order.order_status,
                'order_payment': Order.Payment.portmone,
                'order_shipment': self.order.order_shipment,
                'user': self.order.user.id,
                'order_cost': '0.00',
            }
        )
        print(response.json())
        self.assertEqual(response.status_code, 200)
        created_order = Order.objects.get(id=response.json()['id'])
        self.assertEqual(response.json(), {
            'id': created_order.id,
            'order_number': created_order.order_number,
            'order_date': created_order.order_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            'order_status': created_order.order_status,
            'order_payment': created_order.order_payment,
            'order_shipment': created_order.order_shipment,
            'user': created_order.user.id,
            'order_cost': str(created_order.order_cost),
        })

    def test_patch_order(self):
        print(self.user.id)
        print(self.order.id)
        print(self.orderitem.id)
        print(self.order.order_number)
        response = self.c.patch(
            '/orders/{}/'.format(self.order.id),
            data={
                'order_number': str(uuid.uuid4())[:23],
                'order_payment': Order.Payment.portmone,
            }
        )
        print(type(response.json()))
        self.assertEqual(response.status_code, 200)
        created_order = Order.objects.get(id=response.json()['id'])
        self.assertEqual(response.json(), {
            'id': created_order.id,
            'order_number': created_order.order_number,
            'order_date': created_order.order_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            'order_status': created_order.order_status,
            'order_payment': created_order.order_payment,
            'order_shipment': created_order.order_shipment,
            'user': created_order.user.id,
            'order_cost': str(created_order.order_cost),
        })

    def test_get_order_failed(self):
        response = self.c.get('/orders/100/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'detail': 'Not found.'})

    def test_get_orderitem_failed(self):
        response = self.c.get('/orders/orderitem100/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'detail': 'Not found.'})
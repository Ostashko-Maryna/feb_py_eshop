#from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from apps.orders.models import Order, OrderItem
from django.contrib.auth.models import User
from apps.products.models import Product
from apps.user_profiles.models import UserProfile
import uuid
from django.db.models.deletion import ProtectedError

class OrdersTestAPI(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('user_name', 'user_name@gmail.com', 'password')
        #self.userprofile = UserProfile.objects.create(user=self.user, first_name='Denys', last_name='Kotsiuba', vip_status=True)
        self.product = Product.objects.create(name='test product', created_by=self.user)
        self.order = Order.objects.create(user=self.user)
        self.orderitem = self.order.orderitem.create(order=self.order, product=self.product)
        self.c = APIClient()
        self.maxDiff = None

    def test_1(self):
        print(self.user.id)
        #print(self.userprofile.vip_status)
        print(self.order.id)
        print(self.orderitem.id)
        response = self.c.get('/orders/user1/?limit=1')
        self.assertEqual(response.status_code, 200)
        print(response.json())
        self.assertEqual(response.json(), {
            'count': 1,
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

    def test_2(self):
        print(self.user.id)
        print(self.order.id)
        print(self.orderitem.id)
        response = self.c.get('/orders/2/orderitems/?limit=1')
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [{
                'id': self.orderitem.id,
                'order': self.orderitem.order.id,
                'product': self.orderitem.product.id,
                'amount_of_products': self.orderitem.amount_of_products
            }]
        })

    def test_3(self):
        print(self.user.id)
        print(self.order.id)
        print(self.orderitem.id)
        response = self.c.get('/orders/3/')
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

    def test_4(self):
        print(self.user.id)
        print(self.order.id)
        print(self.orderitem.id)
        response = self.c.get('/orders/orderitem4/')
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'id': self.orderitem.id,
            'order': self.orderitem.order.id,
            'product': self.orderitem.product.id,
            'amount_of_products': self.orderitem.amount_of_products
        })

    def test_5(self):
        print(self.user.id)
        print(self.order.id)
        print(self.orderitem.id)
        response = self.c.post(
            '/orders/user5/',data={
                'user': self.user.id
            }
        )
        print(response.json())
        self.assertEqual(response.status_code, 201)
        created_order = Order.objects.get(id=response.json()['id'])
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

    def test_6(self):
        print(self.user.id)
        print(self.order.id)
        print(self.orderitem.id)
        response = self.c.post(
            '/orders/3/orderitems/', data={
                'order': self.order.id,
                'product': self.product.id
            }
        )
        print(response.json())
        self.assertEqual(response.status_code, 201)
        created_orderitem = OrderItem.objects.get(id=response.json()['id'])
        self.assertEqual(response.json(), {
            'id': created_orderitem.id,
            'order': created_orderitem.order.id,
            'product': created_orderitem.product.id,
            'amount_of_products': created_orderitem.amount_of_products
        })

    def test_7(self):
        print(self.user.id)
        print(self.order.id)
        print(self.orderitem.id)
        print(self.order.order_number)
        response = self.c.put(
            '/orders/8/',
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

    def test_8(self):
        print(self.user.id)
        print(self.order.id)
        print(self.orderitem.id)
        response = self.c.put(
            '/orders/orderitem9/',
            data={
                'id': self.orderitem.id,
                'order': self.orderitem.order.id,
                'product': self.orderitem.product.id,
                'amount_of_products': 2
            }
        )
        print(response.json())
        self.assertEqual(response.status_code, 200)
        created_orderitem = OrderItem.objects.get(id=response.json()['id'])
        self.assertEqual(response.json(), {
            'id': created_orderitem.id,
            'order': created_orderitem.order.id,
            'product': created_orderitem.product.id,
            'amount_of_products': created_orderitem.amount_of_products
        })

    def test_9(self):
        print(self.user.id)
        print(self.order.id)
        print(self.orderitem.id)
        print(self.order.order_number)
        response = self.c.patch(
            '/orders/10/',
            data={
                'order_number': str(uuid.uuid4())[:23],
                'order_payment': Order.Payment.portmone,
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

    def test_90(self):
        print(self.user.id)
        print(self.order.id)
        print(self.orderitem.id)
        response = self.c.patch(
            '/orders/orderitem11/',
            data={
                'amount_of_products': 20
            }
        )
        print(response.json())
        print(response)
        self.assertEqual(response.status_code, 200)
        created_orderitem = OrderItem.objects.get(id=response.json()['id'])
        self.assertEqual(response.json(), {
            'id': created_orderitem.id,
            'order': created_orderitem.order.id,
            'product': created_orderitem.product.id,
            'amount_of_products': created_orderitem.amount_of_products
        })

    def test_91(self):
        print(self.user.id)
        print(self.order.id)
        print(self.orderitem.id)
        with self.assertRaises(ProtectedError):
            response = self.c.delete('/orders/12/')

    def test_92(self):
        print(self.user.id)
        print(self.order.id)
        print(self.orderitem.id)
        response = self.c.delete('/orders/orderitem13/')
        print(response.status_code)
        print(response)
        self.assertEqual(response.status_code, 204)


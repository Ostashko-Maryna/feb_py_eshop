#from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from apps.orders.models import Order, OrderItem
from django.contrib.auth.models import User
from apps.products.models import Product

class OrdersTestAPI(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('user_name', 'user_name@gmail.com', 'password')
        self.order1 = Order.objects.create(user=self.user)
        self.order2 = Order.objects.create(user=self.user)
        self.product = Product.objects.create(name='test product', created_by=self.user)
        self.orderitem1 = self.order1.orderitem.create(product = self.product)
        self.orderitem2 = self.order1.orderitem.create(product=self.product)
        self.c = APIClient()

    def test_order_list(self):
        response = self.c.get('/orders/user1/?limit=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'count': 2,
            'next': 'http://testserver/orders/user1/?limit=1&offset=1',
            'previous': None,
            'results': [{
                'id': self.order1.id,
                'order_number': self.order1.order_number,
                'order_date': self.order1.order_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                'order_status': self.order1.order_status,
                'order_payment': self.order1.order_payment,
                'order_shipment': self.order1.order_shipment,
                'user': self.order1.user.id,
                'order_cost': '0.00',
            }]
        })

    def test_post_to_order_list(self):
        
        response = self.c.post('/orders/user1/')
        print((response.json().get('id')))
        print(response.json())
        print('__'*30)
        self.assertEqual(response.status_code, 201)
        created_order = Order.objects.get(id=response.json().get('id'))
        print(created_order)
        #FIXME: add validation against obj form db
        self.assertEqual(response.json(), {
            'id': created_order.id,
            'order_number': created_order.order_number,
            'order_date': response.json().get('order_date'),
            'order_status': response.json().get('order_status'),
            'order_payment': response.json().get('order_payment'),
            'order_shipment': response.json().get('order_shipment'),
            'user': response.json().get('user'),
            'order_cost': response.json().get('order_cost'),
        })

    def test_orderitem_list(self):
        response = self.c.get('/orders/3/orderitems/?limit=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'count': 2,
            'next': 'http://testserver/orders/3/orderitems/?limit=1&offset=1',
            'previous': None,
            'results': [{
                'id': self.orderitem1.id,
                'order': self.orderitem1.order.id,
                'product': self.orderitem1.product.id,
                'amount_of_products': self.orderitem1.amount_of_products
            }]
        })

    def test_post_to_orderitem_list(self):
        response = self.c.post('/orders/3/orderitems/')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
            'id': response.json().get('id'),
            'order': response.json().get('order'),
            'product': response.json().get('product'),
            'amount_of_products': response.json().get('amount_of_products')
        })

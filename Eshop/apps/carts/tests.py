from rest_framework.test import APIClient, APITestCase
from apps.carts.models import Cart, CartItem
from django.contrib.auth.models import User
from apps.products.models import Product

def login_user(client, user, password='cartnamepwrd'):
    client.login(username=user.username, password=password)

class CartTestAPI(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('cartname', 'cartname@yyy.yyy', 'cartnamepwrd',)
        self.product = Product.objects.create(vendor_code='1111',
                                              name='product_in_cart', 
                                              created_by=self.user,
                                              price=1111, 
                                              stock_count=1111,
                                              description='numbers', 
                                              characteristics='1111',
                                              available=True, )
        self.cart = Cart.objects.create(user=self.user)
        self.cartitem = CartItem.objects.create(user=self.user, 
                                                product=self.product, 
                                                cart=self.cart)     
        self.c = APIClient()
        self.maxDiff = None


    def test_get_cart(self):
        print(self.user.id)
        print(self.cart.id)
        # print(self.cartitem.id)
        login_user(self.c, self.user)
        response = self.c.get('/cart/1/')
        self.assertEqual(response.status_code, 200)
        print(response.json())
        test_data = {
                'id': self.cart.id, 
                'user': self.cart.user.id, 
                'not_empty': self.cart.not_empty, 
                'created_on': self.cart.created_on.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                'updated_on': self.cart.updated_on.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                'total_price': self.cart.total_price, 
                'cart_list': self.cart.cart_list, 
                'not_available': self.cart.not_available
        }

        for key, value in response.json().items():
            print(key)
            print(test_data[key]==value)
            if not test_data[key]==value:
                print(test_data[key])
                print(value)

        self.assertEqual(response.json(), {
                'id': self.cart.id, 
                'user': self.cart.user.id, 
                'not_empty': self.cart.not_empty, 
                'created_on': self.cart.created_on.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                'updated_on': self.cart.updated_on.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                'total_price': self.cart.total_price, 
                'cart_list': self.cart.cart_list, 
                'not_available': self.cart.not_available
        })

    def test_get_cartitem(self):
        print(self.user.id)
        print(self.cart.id)
        print(self.cartitem.id)

        login_user(self.c, self.user)
        response = self.c.get('/cart/1/cartitem/')
        print(response.json())
        self.assertEqual(response.status_code, 200)
        print(response.json())
        self.assertEqual(response.json(), {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [{
                'id': self.cartitem.id,
                'user': self.cart.user.id,
                'product': 
                    {
                    'id': 1,
                    'vendor_code': '1111',
                    'name': 'product_in_cart', 
                    'created_by': None,
                    'updated_by': None,
                    'price': 1111, 
                    'stock_count': 1111,
                    'description': 'numbers', 
                    'characteristics': '1111',
                    'available': True, 
                    },
                'quantity': 1,
                'updated_by': None,
                'updated_on': '2020-06-13T10:49:12.476649Z',

                'cart': self.cartitem.cart.id,
                'created_on': self.cartitem.created_on.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                'not_empty': self.cart.not_empty,
                'total_price': self.cart.total_price,
            }]
        })

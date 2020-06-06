from rest_framework.test import APIClient, APITestCase
from apps.carts.models import Cart, CartItem
from django.contrib.auth.models import User
from apps.products.models import Product

class CartTestAPI(APITestCase):
    def setUp(self):
        
        self.user = User.objects.create_user('cartname', 'cartname@cart.cart', 'cartname')
        self.product = Product.objects.create(vendor_code='1111',
                                              name='product_in_cart', 
                                              created_by=self.user,
                                              price=1111, 
                                              stock_count=1111,
                                              description='numbers', 
                                              characteristics='1111',
                                              available=True, )
        self.cart = Cart.objects.create(user=self.user)
        self.cartitem = self.cartitem.create(product=self.product, cart=self.cart)
        self.c = APIClient()
        self.maxDiff = None

    def get_cart(self):
        print(self.user.id)
        print(self.cart.id)
        response = self.c.get('/cart/1/1/')
        self.assertEqual(response.status_code, 200)
        print(response.json())
        self.assertEqual(response.json(), {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [{
                'id': self.cart.id,
                'user': self.cart.user.id,
                'cart_number': self.cart.cart_number,
                'created_on': self.cart.created_on.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                'not_empty': self.cart.not_empty,
            }]
        })
        
    def get_cartitem(self):
        print(self.user.id)
        print(self.cart.id)
        print(self.cartitem.id)
        response = self.c.get('/carts/1/1/1/')
        self.assertEqual(response.status_code, 200)
        print(response.json())
        self.assertEqual(response.json(), {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [{
                'id': self.cart.id,
                'user': self.cart.user.id,
                'product': self.cartitem.product,
                'cart': self.cartitem.cart,
                'created_on': self.cart.created_on.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                'not_empty': self.cart.not_empty,
                'total_price': '1111.00',
            }]
        })
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Product, Review, Kit


class ProductsTestAPI(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user_1', 'user_1@gmail.com', 'password')
        self.product = Product.objects.create(vendor_code='Art_1', name='Product_1', price=500, stock_count=21,
                                              description='Good product ...', characteristics='1x2x3',
                                              available=True, created_by=self.user)
        self.client = APIClient()
        print(self.user)
        print(self.product)

    def test_get_products_list(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        print(response.json())
        self.assertEqual(response.json(), [{
            'id': self.product.id,
            'vendor_code': self.product.vendor_code,
            'name': self.product.name,
            'price': self.product.price,
            'stock_count': self.product.stock_count,
            'description': self.product.description,
            'characteristics': self.product.characteristics,
            'available': self.product.available,
            'created_by': self.product.created_by.id
        }])

    # def test_list_paged(self):
    #     c = APIClient()
    #     response = self.c.get('/products/?limit=3')
    #     self.assertEqual(response.status_code, 200)
    #     # print(response.json())


class ReviewsTestAPI(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user_2', 'user_2@gmail.com', 'password')
        self.product = Product.objects.create(vendor_code='Art_2', name='Product_2', price=700, stock_count=71,
                                              description='Perfect product ...', characteristics='11x22x33',
                                              available=True, created_by=self.user)
        self.review = Review.objects.create(product=self.product, user=self.user,
                                            review='product_2 is cool', available=True)
        self.client = APIClient()
        print(self.user)
        print(self.product)
        print(self.review)

    def test_get_reviews_list(self):
        response = self.client.get('/products/reviews/')
        self.assertEqual(response.status_code, 200)
        print(response.json())
        self.assertEqual(response.json(), [{
            'id': self.review.id,
            'product': self.product.id,
            'user': self.review.user.id,
            'review': self.review.review,
            'available': self.review.available,
        }])


class KitsTestAPI(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user_3', 'user_3@gmail.com', 'password')
        self.product_3 = Product.objects.create(vendor_code='Art_3', name='Product_3', price=900, stock_count=9,
                                                description='Super product ...', characteristics='3x2x1',
                                                available=True, created_by=self.user)
        self.product_4 = Product.objects.create(vendor_code='Art_4', name='Product_4', price=100, stock_count=10,
                                                description='Light product ...', characteristics='30x20x10',
                                                available=True, created_by=self.user)
        self.kit = Kit.objects.create(description='Sale ...', available=True,
                                      term='2020-05-20 13:16:14.70362+00',
                                      created_by=self.user)
        self.client = APIClient()
        print(self.user)
        print(self.product_3)
        print(self.kit)

    def test_get_kits_list(self):
        response = self.client.get('/products/kits/')
        self.assertEqual(response.status_code, 200)
        print(response.json())
        self.assertEqual(response.json(), [{
            'id': self.kit.id,
            'products': [],
            'description': self.kit.description,
            'available': self.kit.available,
            'term': '2020-05-20T13:16:14.703620Z',
            'created_by': self.kit.created_by.id
        }])

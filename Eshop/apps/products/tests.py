from django.test import TestCase
from rest_framework.test import APIClient
from apps.products.models import Product

class ProductsTestAPI(TestCase):
    def setUp(self):
        self.p = Product.objects.create(name='testp', description='asd')
        self.c = APIClient()

    def test_list(self):
        response = self.c.get('/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{
            'id': self.p.id, 
            'vendor_code': '', 
            'name': self.p.name, 
            'price': 0.0, 
            'stock_count': 0, 
            'description': self.p.description, 
            'characteristics': '', 
            'available': True, 
            'created_by': None
        }])


    def test_list_paged(self):
        c = APIClient()
        response = self.c.get('/products/?limit=3')
        self.assertEqual(response.status_code, 200)
        # print(response.json())

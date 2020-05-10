import os

from django.conf import settings
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from apps.galleries.models import Gallery
from apps.products.models import Product

class GalleryTestAPI(TestCase):
    def setUp(self):
        p1 = Product.objects.create(name='testp', description='asd')
        # p2 = Product.objects.create(name='testp', description='asd')
        self.g1 = Gallery.objects.create(product=p1, name='test_g1', image='photo1.jpg')
        # self.g2 = Gallery.objects.create(product=p2, name='test_g2', image='photo2.jpg')
        self.c = APIClient()


    def test_get_gallery(self):
        response = self.c.get('/galleries/1/1/')
        self.assertEqual(response.status_code, 200)
        # print("="*59)
        # print(response.json())
        self.assertEqual(response.json(), {
            'id': 1, 
            'product': 1, 
            'name': 'test_g1', 
            'url': None, 
            'size': 'middle', 
            'size_x': 150, 
            'size_y': 150
        })

    def test_post_gallery(self):
        with open(os.path.join(settings.STATIC_ROOT, 'test', 'image_file.jpg'), mode='rb') as fp:
            response = self.c.post(
                '/galleries/',
                data={
                    "product": "1",
                    "name": "image_test",
                    "image": fp,
                    "size": "min",
                    "size_x": "50",
                    "size_y": "50"
                }
            )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # print("="*59)
        # print(response.json())
        self.assertEqual(response.json(), {
            'id': 2, 
            'product': 1, 
            'name': 'image_test', 
            'url': 'product_photos/2020/05/10/image_file.jpg', 
            'size': 'min', 
            'size_x': 50, 
            'size_y': 50
        })

    def test_product_gallereis_list(self):
        response = self.c.get('/galleries/1/')
        self.assertEqual(response.status_code, 200)
        # print("="*59)
        # print(response.json())
        self.assertEqual(response.json(), [{
            'id': 1, 
            'product': 1, 
            'name': 'test_g1', 
            'url': None, 
            'size': 'middle', 
            'size_x': 150, 
            'size_y': 150
        }])


    def test_get_gallery(self):
            response = self.c.get('/galleries/1/2/') # {'detail': 'Not found.'}
            self.assertEqual(response.status_code, 200) # AssertionError: 404 != 200
            print("="*59)
            print(response.json())  # FAILED (failures=1)
                                   


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
        self.g2 = Gallery.objects.create(product=p1, name='test_g2', image='photo2.jpg', size = 'max')
        self.c = APIClient()


    def test_get_galleries_list(self):
        response = self.c.get('/galleries/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{
                'product': {
                    'id': 1, 
                    'name': 'testp'
                }, 
                'id': 1, 
                'name': 'test_g1', 
                'url': '/static/pictures/no_product.png', # 'D:\\My_doc\\Programing\\Django\\feb_py_eshop\\Eshop\\photo1.jpg'
                'size': 'middle', 
                'size_x': 150, 
                'size_y': 150
            }, {
                'product': {
                    'id': 1, 
                    'name': 'testp'
                }, 
                'id': 2, 
                'name': 'test_g2', 
                'url': '/static/pictures/no_product.png', # 'D:\\My_doc\\Programing\\Django\\feb_py_eshop\\Eshop\\photo2.jpg'
                'size': 'max', 
                'size_x': 250, 
                'size_y': 250
        }])


    def test_product_gallereis_pagination_list(self):
        response = self.c.get('/galleries/1/?limit=1&offset=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'count': 2, 
            'next': None, 
            'previous': 'http://testserver/galleries/1/?limit=1', 
            'results': [{
                'product': {
                    'id': 1, 
                    'name': 'testp'
                }, 
                'id': 2, 
                'name': 'test_g2', 
                'url': '/static/pictures/no_product.png', 
                'size': 'max', 
                'size_x': 250, 
                'size_y': 250
            }]
        })
    

    def test_get_gallery(self):
        response = self.c.get('/galleries/1/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'product': {
                'id': 1, 
                'name': 'testp'
            }, 
            'id': 1, 
            'name': 'test_g1', 
            'url': '/static/pictures/no_product.png', 
            'size': 'middle', 
            'size_x': 150, 
            'size_y': 150
        })


    def test_post_gallery(self):
        p1 = Product.objects.create(name='other product', description='asd')
        with open(os.path.join(settings.STATIC_ROOT, 'test', 'image_file.jpg'), mode='rb') as fp:
            response = self.c.post(
                '/galleries/1/',
                data={
                    "product": p1.id,
                    "name": "test_post_g",
                    "image": fp,
                    "size": "min",
                } 
            )
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_object = Gallery.objects.get(id=response.json()['id'])
        self.assertEqual(response.json(), {
            'product': {
                'id': p1.id, 
                'name': p1.name
            }, 
            'id': created_object.id, 
            'name': 'test_post_g', 
            'url': created_object.image_url, 
            'size': 'min', 
            'size_x': 50, 
            'size_y': 50
        })


    def test_get_gallery_failed(self):
        response = self.c.get('/galleries/1/3/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {
            'detail': 'Not found.'
        })


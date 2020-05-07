from django.test import TestCase
from rest_framework.test import APIClient
from apps.galleries.models import Gallery
from apps.products.models import Product

class GalleryTestAPI(TestCase):
	def setUp(self):
		p1 = Product.objects.create(name='testp', description='asd')
		p2 = Product.objects.create(name='testp', description='asd')
		self.g1 = Gallery.objects.create(product=p1, name='test_g1', image='photo1.jpg')
		self.g2 = Gallery.objects.create(product=p2, name='test_g2', image='photo2.jpg')
		self.c = APIClient()

	def test_list(self):
		response = self.c.get('/galleries/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json(), [{
			'id': 1, 
			'product': 1, 
			'name': 'test_g1', 
			'image': 'http://testserver/galleries/photo1.jpg', 
			'size': 'middle', 
			'size_x': None, 
			'size_y': None
		}, {
			'id': 2, 
			'product': 2, 
			'name': 'test_g2', 
			'image': 'http://testserver/galleries/photo2.jpg', 
			'size': 'middle', 
			'size_x': None, 
			'size_y': None
		}])

	def test_product_images_list(self):
		response = self.c.get('/galleries/2/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json(), [{
			'id': 2, 
			'product': 2, 
			'name': 'test_g2', 
			'image': 'http://testserver/galleries/2/photo2.jpg', 
			'size': 'middle', 
			'size_x': None, 
			'size_y': None
		}])

	def test_gallery(self):
		response = self.c.get('/galleries/1/2/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json(), {
			'id': 2, 
			'product': 2, 
			'name': 'test_g2', 
			'image': 'http://testserver/galleries/1/2/photo2.jpg', 
			'size': 'middle', 
			'size_x': None, 
			'size_y': None
		})

	# def test_list_post(self):
	# 	print('==================')
	# 	with open('photo3.jpg', 'rb') as fp:
	# 		response = self.c.post('/galleries/', {'name': 'test_post', 'product': 2, 'image': 'fp'}, format='json')
	# 	print(response.status_code, response.json())

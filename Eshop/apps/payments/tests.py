from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Payments
from apps.orders.models import Order
from datetime import date


class PaymentsTestCase(TestCase):

    maxDiff = None

    def setUp(self):
        self.user = User.objects.create()
        self.order = Order.objects.create(user=self.user)
        self.payment = Payments.objects.create(
            user = self.user,
            order = self.order,
            paymentsystem = 'portmone',
            billAmount = 100.0,
            payment_date = date.today(),
            status = 'completed',
        )
        self.client = APIClient()


    def test_payments_get(self):
        print()
        response = self.client.get('/payments/')
        self.assertEqual(response.status_code, 200)
        print(response.json())
        self.assertEqual(response.json(),{
            'count': 1, 
            'next': None, 
            'previous': None, 
            'results': [{
                'id': self.payment.id,
                'user': self.user.id, 
                'order':{
                    # 'id': self.payment.id,
                    'user': self.user.id,
                    'order_status': self.order.order_status,
                    'order_payment': self.order.order_payment, 
                },
                'paymentsystem': str(self.payment.paymentsystem),
                'billAmount': self.payment.billAmount,
                'payment_date': str(
                    self.payment.payment_date.isoformat().replace('+00:00','Z')
                ),
                'status': str(self.payment.status),
                'permissions': self.payment.permissions(user=self.user.id),
            }]
        })
#TODO
    def test_payments_post(self):
        number =  self.payment.id
        request = self.client.post('/payments/',{
            'user': self.user.id,
            'id': self.payment.id, 
            'payment_date': date.today(), 
            'user': self.user.id, 
            'order': {
                'user': self.user.id,
                'order_status': self.order.order_status,
                'order_payment': self.order.order_payment,
            },
            'paymentsystem': self.payment.paymentsystem,
            'billAmount': self.payment.billAmount,
            'status': self.payment.status,
        })
        print(request.json())

        self.assertEqual(request.status_code, 201)
        
        #getting the posted data from the DB
        # created_id = Payments.objects.get(id = request.json()['id'])
        # self.assertEqual(request.json(),{
            # 'id': created_id.id, 
            # 'payment_date': created_id.payment_date.isoformat().replace(
                # '+00:00', 'Z'
            # ),
            # 'user': created_id.user.id, 
            # 'order': created_id.order.id, 
            # 'paymentsystem': created_id.paymentsystem
        # })


    # def test_payments_detail(self):
        # print()
        # number =  self.payment.id
        # response = self.client.get('/payments/{}/'.format(number))
        # self.assertEqual(response.status_code, 200)
        # print(response.json())
        # self.assertEqual(response.json(),{
            # 'id': self.payment.id, 
            # 'payment_date': str(
                # self.payment.payment_date.isoformat().replace('+00:00', 'Z')
            # ), 
            # 'user': self.user.id, 
            # 'order': self.order.id, 
            # 'paymentsystem': str(self.payment.paymentsystem)
        # })

    # def test_payments_detail_put_patch_del(self):
        # print()
        # number =  self.payment.id
        # request = self.client.put('/payments/{}/'.format(number))
        # self.assertEqual(request.status_code, 200)
        # print(request.json())
        # created_id = Payments.objects.get(id = request.json()['id'])
        # self.assertEqual(request.json(),{
            # 'id': self.payment.id, 
            # 'payment_date': str(
                # self.payment.payment_date.isoformat().replace('+00:00', 'Z')
            # ), 
            # 'user': self.user.id, 
            # 'order': self.order.id, 
            # 'paymentsystem': str(self.payment.paymentsystem)
        # })
        
        # #patching
        # request = self.client.patch('/payments/{}/'.format(number), {
        # 'paymentsystem': 'cash',    
        # })
        # self.assertEqual(request.status_code, 200)
        # print(request.json())
        # self.assertEqual(request.json(),{
            # 'id': self.payment.id, 
            # 'payment_date': str(
                # self.payment.payment_date.isoformat().replace('+00:00', 'Z')
            # ), 
            # 'user': self.user.id, 
            # 'order': self.order.id, 
            # 'paymentsystem': 'cash'
        # })

        # #deleting
        # request = self.client.delete('/payments/{}/'.format(number))
        # self.assertEqual(request.status_code, 204)


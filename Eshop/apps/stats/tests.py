from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from apps.stats.models import Stats
from datetime import date


class StatsTestAPI(TestCase):

    def setUp(self):
        self.user = User.objects.create()
        self.stats = Stats.objects.create(
            user=self.user,
            action_date=date.today(),
            data={'Action': 'View',
                  'Product': 'Product_2'
                  }
        )
        self.c = APIClient()
        self.maxDiff = None

    def test_stats_list_get(self):
        response = self.c.get('/stats/')
        self.assertEqual(response.status_code, 200)
        # print(response.json())
        self.assertEqual(response.json(), {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [{
                'id': self.stats.id,
                'user': self.user.id,
                'data': {'Action': 'View',
                         'Product': 'Product_2'}
            }]}
                         )

    def test_stats_list_detail_get(self):
        # print(self.stats.id)
        response = self.c.get('/stats/{}'.format(self.stats.id))
        self.assertEqual(response.status_code, 200)
        # print(response.json())
        self.assertEqual(response.json(), {'data': {'Action': 'View',
                                                    'Product': 'Product_2'},
                                           'id': self.stats.id,
                                           'user': self.user.id}
                         )

    def test_stats_list_filter(self):
        # print(self.stats.id)
        response = self.c.get('/stats/?id={}&user=&action=&product='.format(self.stats.id))
        self.assertEqual(response.status_code, 200)
        print(response.json())
        self.assertEqual(response.json(), {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [{
                'id': self.stats.id,
                'user': self.user.id,
                'data': {'Action': 'View',
                         'Product': 'Product_2'}
            }]}
                         )

    def test_stats_post(self):
        response = self.c.post('/stats/', data={
            'data': {"Action": "View",
                     "Product": "Product_2"},
            'id': self.stats.id,
            'user': self.user.id
        },
                               format='json'
                               )
        # print(response.json())
        self.assertEqual(response.status_code, 201)
        created_obj = Stats.objects.get(id=response.json()['id'])
        self.assertEqual(response.json(), {
            'id': created_obj.id,
            'user': created_obj.user.id,
            'data': {'Action': 'View',
                     'Product': 'Product_2'}
        })

    def test_stats_put(self):
        response = self.c.put('/stats/{}'.format(self.stats.id),
                              data={'id': self.stats.id,
                                    'user': self.user.id,
                                    'data': {'Action': 'View',
                                             'Product': 'Product5'}},
                              format='json')
        self.assertEqual(response.status_code, 200)
        print(response.json())
        created_obj = Stats.objects.get(id=response.json()['id'])
        self.assertEqual(response.json(), {
            'id': created_obj.id,
            'user': created_obj.user.id,
            'data': {'Action': 'View',
                     'Product': 'Product5'}
        })

    def test_stats_patch(self):
        response = self.c.patch('/stats/{}'.format(self.stats.id),
                                data={'id': self.stats.id,
                                      'user': self.user.id,
                                      'data': {'Action': 'Buy',
                                               'Product': 'Product_2',
                                               'Sales Price': 134,
                                               'Sales Amount': 23,
                                               'Total sales': 3082}},
                                format='json')
        self.assertEqual(response.status_code, 200)
        print(response.json())
        created_obj = Stats.objects.get(id=response.json()['id'])
        self.assertEqual(response.json(), {
            'id': created_obj.id,
            'user': created_obj.user.id,
            'data': {'Action': 'Buy',
                     'Product': 'Product_2',
                     'Sales Price': 134,
                     'Sales Amount': 23,
                     'Total sales': 3082}
        })

    def test_stats_list_datail_not_found(self):
        response = self.c.get('/stats/5')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'detail': 'Not found.'})

    def test_stats_delete(self):
        response = self.c.delete('/stats/{}'.format(self.stats.id))
        self.assertEqual(response.status_code, 204)

from django.conf import settings
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import UserProfile, DeliveryAddress
from django.core.files.uploadedfile import SimpleUploadedFile


class UserProfileTestApi(TestCase):

    def setUp(self):
        #UserProfile.objects.created()
        self.client = APIClient
        self.test_user1 = User.objects.create_user(
            username='test_user1', password='password1')
        self.test_user2 = User.objects.create_user(
            username='test_user2', password='password2')
        photo_test = SimpleUploadedFile(name='photo_test.jpg', content=open('static/test/photo_test.jpg', 'rb').read(), content_type='image/jpeg')
        self.user_profile1 = UserProfile.objects.create(user=self.test_user1,
                                                        date_of_birth="1994-08-07",
                                                        phone_number=444444444,
                                                        photo=photo_test,
                                                        vip_status=True)
        self.user_profile2 = UserProfile.objects.create(user=self.test_user2,
                                                        date_of_birth="1995-09-03",
                                                        phone_number=5555555555,
                                                        photo=photo_test,
                                                        vip_status=False)

    def test_get_user_profiles_list(self):
        response = self.client.get('/user_profiles/')
        self.assertEqual(response.status_code, 200)
        print('I'*100)
        print(response.json())
        print('I' * 100)
        """
        self.assertEqual(response.json(), {
            "count": 2,
            "next": null,
            "previous": null,
            "results": [
                {
                    "id": 1,
                    "user": 1,
                    "date_of_birth": "1994-08-07",
                    "phone_number": 444444444,
                    "vip_status": true
                },
                {
                    "id": 2,
                    "user": 2,
                    "date_of_birth": "1995-09-03",
                    "phone_number": 5555555555,
                    "vip_status": false
                }
            ]
        })
        """
        #self.assertEqual(response.json(),

    #def test_first_name_max_length(self):
    #    author = Author.objects.get(id=1)
    #    max_length = author._meta.get_field('first_name').max_length
    #    self.assertEquals(max_length, 100)

    #def test_object_name_is_last_name_comma_first_name(self):
    #    user_profile = UserProfile.objects.get(id=1)
    #    expected_object_name = '{} {}'.format(self.user_profile.first_name, self.user.last_name)
    #    self.assertEquals(expected_object_name, str(user_profile))
#
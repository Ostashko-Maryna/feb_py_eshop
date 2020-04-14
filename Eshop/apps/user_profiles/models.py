from django.db import models


class UserProfile(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    delivery_address = models.CharField(max_length=200)
    vip_status = models.BooleanField(default=False)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

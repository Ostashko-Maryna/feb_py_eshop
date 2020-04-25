from django.db import models
#from localflavor import ua


class UserProfile(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.BigIntegerField(null=True)
    photo = models.ImageField(upload_to='static/users/%Y/%m/%d', blank=True)
    vip_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class DeliveryAddress(models.Model):
    user = models.ForeignKey('UserProfile', null=True, on_delete=models.CASCADE)
    region = models.CharField(max_length=200, null=True,)
    city = models.CharField(max_length=200, null=True,)
    street = models.CharField(max_length=200, null=True,)
    house_number = models.BigIntegerField(null=True)
    apartment_number = models.BigIntegerField(null=True)
    zip_code = models.CharField(max_length=200, null=True,)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

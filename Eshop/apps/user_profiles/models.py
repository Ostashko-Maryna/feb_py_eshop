from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from localflavor import ua


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.BigIntegerField(null=True)
    photo = models.ImageField(upload_to='static/users/%Y/%m/%d', blank=True)
    vip_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.user_profile.save()


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

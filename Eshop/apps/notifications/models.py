from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    methods = [
        ('mail', 'Mail'),
        ('sms', 'SMS'),
        ('telegram', 'Telegram'),
        ('viber', 'Viber'),
    ]
    notify_receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    notify_method = models.CharField(max_length=10, choices=methods, default='mail')
    notify_title = models.CharField(max_length=100, null=None)
    notify_message = models.CharField(max_length=200)
    notify_date = models.DateTimeField('date published')

    def __str__(self):
        return '{} {} {}'.format(self.notify_receiver, self.notify_method, self.notify_title)

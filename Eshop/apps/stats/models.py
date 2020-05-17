from django.contrib.postgres.fields import JSONField
from django.db import models


class Stats(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    action_date = models.DateTimeField(auto_now_add=True)
    data = JSONField()



from django.contrib import admin
from .models import Payments, PaymentSystemLog

admin.site.register(Payments)
admin.site.register(PaymentSystemLog)

from django.contrib import admin
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Receiver', {'fields': ['notify_receiver', 'notify_method']}),
        ('Message', {'fields': ['notify_title', 'notify_message']}),
        ('Date', {'fields': ['notify_date']}),
    ]
    list_display = ('notify_receiver', 'notify_title', 'notify_message', 'notify_date', 'notify_method')
    list_filter = ['notify_receiver']
    search_fields = ['notify_receiver']


admin.site.register(Notification, NotificationAdmin)

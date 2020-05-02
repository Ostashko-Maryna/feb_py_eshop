from django.contrib import admin
from .models import Payments, PaymentSystemLog
from django.contrib.postgres.fields import JSONField
from django_json_widget.widgets import JSONEditorWidget

class JsonAdmin(admin.ModelAdmin):
	formfield_overrides = {
		JSONField: {'widget': JSONEditorWidget},
	}

admin.site.register(Payments)
admin.site.register(PaymentSystemLog, JsonAdmin)

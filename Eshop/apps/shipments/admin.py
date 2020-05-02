from django.contrib import admin
from .models import Shipment

class ShipmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Shipment, ShipmentAdmin)

from django.contrib import admin
from .models import Shipment

class ShipmentAdmin(admin.ModelAdmin):
    raw_id_fields = ("order",)

    list_display = (
        'order',
        'shipment_id',
        'shipment_address_city',
        'shipment_status_date_created'
    )

admin.site.register(Shipment, ShipmentAdmin)
admin.site.disable_action('delete_selected')
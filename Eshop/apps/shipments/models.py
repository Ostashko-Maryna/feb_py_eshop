import uuid
import datetime
from django.db import models
from django.utils import timezone
# from apps.user_profiles.models import UserProfile

class Shipment(models.Model):
    order = models.ForeignKey('orders.Order', on_delete = models.CASCADE)
    shipment_id = models.UUIDField(default=uuid.uuid4, editable=False)
    shipment_status_date_created = models.DateTimeField(auto_now_add = True)
    shipment_status_date_updated = models.DateTimeField(auto_now = True)
    shipment_address_region = models.CharField(max_length = 50, null = True)
    shipment_address_city = models.CharField(max_length = 50)
    shipment_adress_street = models.CharField(max_length = 50)
    shipment_adress_house = models.CharField(max_length = 10)
    shipment_adress_apartment = models.PositiveSmallIntegerField(null = True, blank = True)
    # user_profile = models.OneToOneField(UserProfile,on_delete = models.CASCADE, primary_key = True)
    # shipment_phone_number = user_profile.phone_number

    shipment_comment = models.TextField(blank = True)

    class Shipment_variants:
        pickup = 'Pick_up'
        courier = 'Courier'
        novaposhta = 'Nova_poshta'

    variants_list = [
        (Shipment_variants.pickup, 'Pick up'),
        (Shipment_variants.courier, 'Courier'),
        (Shipment_variants.novaposhta,'Nova Poshta'),
        ]
    variants = models.CharField(max_length=20, default = Shipment_variants.pickup, choices=variants_list)

    def short_uuid(word):
        a = word.split("-")
        return a[len(a)-1]

    def __str__(self):
        return 'Order №{}'.format(Shipment.short_uuid(str(self.shipment_id)))

class ShipmentLog():
    pass



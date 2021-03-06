import uuid
import datetime
from django.db import models
from django.utils import timezone

class Shipment(models.Model):
    order = models.OneToOneField('orders.Order', on_delete = models.CASCADE,related_name = 'order')
    shipment_id = models.UUIDField(default=uuid.uuid4, editable=False)
    shipment_status_date_created = models.DateTimeField(auto_now_add = True)
    shipment_status_date_updated = models.DateTimeField(auto_now = True)
    shipment_address_region = models.CharField(max_length = 50, null = True)
    shipment_address_city = models.CharField(max_length = 50)
    shipment_adress_street = models.CharField(max_length = 50)
    shipment_adress_house = models.CharField(max_length = 10)
    shipment_adress_apartment = models.PositiveSmallIntegerField(null = True, blank = True)
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


    def __str__(self):
        return 'Order №{}'.format(self.shipment_id)

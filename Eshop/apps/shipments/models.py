import uuid
from django.db import models
# from apps.orders.models import Order

class Shipment(models.Model):
    order = models.ForeignKey('orders.Order', on_delete = models.CASCADE)
    shipment_id = models.UUIDField(default=uuid.uuid4, editable=False)
    shipment_status_date = models.DateTimeField(auto_now = True)
    shipment_address_city = models.CharField(max_length = 30)
    shipment_adress_street = models.CharField(max_length = 30)
    shipment_adress_house = models.CharField(max_length = 10)
    shipment_adress_apartment = models.PositiveSmallIntegerField(null = True, blank = True)
    # delivery_phone_number = models.ForeignKey(Order.phone_number,on_delete = models.CASCADE)

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

    # def for_str(word):
        # a = word.split("-")
        # return a[len(a)-1]

    def __str__(self):
        return 'Order {}'.format(self.shipment_id)

class ShipmentLog():
    pass


# notify message for user, notify response
#TODO
# sdf
# sdf

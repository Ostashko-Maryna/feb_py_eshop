import uuid
from django.db import models
from apps.payments.models import Payments #added by Payments performer

class Order(models.Model):
    order_number = models.UUIDField(default=uuid.uuid4, editable=True)
    order_date = models.DateTimeField(auto_now_add=True)
    class Status:
        new = 'New order'
        processing = 'Order processing'
        packing = 'Packing'
        finished = 'Finished'
    status_list = [
        (Status.new, 'New order'),
        (Status.processing, 'Order processing'),
        (Status.packing, 'Packing'),
        (Status.finished, 'Finished'),
    ]
    order_status = models.CharField(max_length=100, default=Status.new, choices=status_list)
    class Payment:
        cash = 'Cash'
        portmone = 'Portmone'
    payment_list = [
        (Payment.cash, 'Cash'),
        (Payment.portmone, 'Portmone'),
    ]
    order_payment = models.CharField(max_length=100, blank=False, choices=payment_list)
    class Shipment:
        pickup = 'Pickup'
        new_post = 'New Post'
    shipment_list = [
        (Shipment.pickup, 'Pickup'),
        (Shipment.new_post, 'New Post'),
    ]
    order_shipment = models.CharField(max_length=100, blank=False, choices=shipment_list)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT, default=None)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.PROTECT)
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT)
    amount_of_products = models.PositiveSmallIntegerField(default=1)
    discont = models.PositiveSmallIntegerField(default=0)

Payments.create_payment(user = 'auth.User', order = Order.order_number) #added by Payments performer

import uuid
from django.db import models
from datetime import datetime

class Order(models.Model):
    def short_order_number():
        return str(uuid.uuid4())[0:23]
    order_number = models.CharField(max_length=30, default=short_order_number, editable=True)
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
    order_payment = models.CharField(max_length=100, blank=False, default=Payment.cash, choices=payment_list)
    class Shipment:
        pickup = 'Pickup'
        new_post = 'New Post'
    shipment_list = [
        (Shipment.pickup, 'Pickup'),
        (Shipment.new_post, 'New Post'),
    ]
    order_shipment = models.CharField(max_length=100, blank=False, default=Shipment.pickup, choices=shipment_list)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT, null=True, blank=False, related_name='order')
    order_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return str(self.order_number)

    def save(self, *args, **kwargs):
        self.order_cost = sum([oi.sell_price for oi in self.orderitem.all()])
        super().save(*args, **kwargs)            

    def __str__(self):
        return str(self.order_number)

class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.PROTECT, null=True, blank=False, related_name='orderitem')
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT, null=True, blank=False)
    amount_of_products = models.PositiveSmallIntegerField(default=1)

    @property
    def sell_price(self):
        if self.order.user.userprofile.vip_status:
            return self.product.price * self.amount_of_products * 0.5
        if str(self.order.user.userprofile.date_of_birth.strftime("%m-%d")) == datetime.now().strftime("%m-%d"):
            return self.product.price * self.amount_of_products * 0.7
        elif self.amount_of_products >= 5:
            return self.product.price * self.amount_of_products * 0.9
        return self.product.price * self.amount_of_products

    def __str__(self):
        return 'Product "{}" in Order #{}'.format(self.product, self.order)


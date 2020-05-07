import uuid
from django.db import models

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

    user = models.ForeignKey('auth.User', on_delete=models.PROTECT, null=True, blank=False, related_name='order')
    order_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def save(self, *args, **kwargs):
        self.order_cost = sum([oi.sell_price for oi in self.orderitem.all()])
        super().save(*args, **kwargs)            


    def __str__(self):
        return str(self.order_number)

class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.PROTECT, null=True, blank=False, related_name='orderitem')
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT, null=True, blank=False)
    amount_of_products = models.PositiveSmallIntegerField(default=1)
    discont = models.PositiveSmallIntegerField(default=0)

    @property
    def sell_price(self):
        if self.order.user.user_profile.vip_status:
            return self.product.price * self.amount_of_products * 0.5
        return self.product.price * self.amount_of_products * ((100-self.discont) / 100)

    def __str__(self):
        return 'Product "{}" in Order #{}'.format(self.product, self.order)

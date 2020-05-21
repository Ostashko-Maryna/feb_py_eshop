from django.db import models
from django.contrib.postgres.fields import JSONField
from django_fsm import FSMField, transition

paymentsystem_list = [
    ('portmone', 'portmone'),
    ('cash', 'cash'),
]

class Status:
    submitted = 'submitted'
    processing = 'processing'
    completed = 'completed'
    suspended = 'suspended'     
    declined = 'declined'

status_list = [
    (Status.submitted, 'submitted'),
    (Status.processing, 'processing'),
    (Status.completed, 'completed'),
    (Status.suspended, 'suspended'),
    (Status.declined, 'declined'),
]


class Payments(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT, 
        null=True, blank=False
    )
    order = models.ForeignKey('orders.Order', on_delete=models.PROTECT,
        null=True, blank=False
    )
    paymentsystem = models.CharField(max_length=10, 
        choices=paymentsystem_list, default='portmone'
    )
    billAmount = models.FloatField(default=0.0)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = FSMField(default=status_list[0], choices=status_list)
    
    
    # ~ class Status:
        # ~ submitted = 'submitted'
        # ~ processing = 'processing'
        # ~ completed = 'completed'
        # ~ suspended = 'suspended'     
        # ~ declined = 'declined'
    
    # ~ status_list = [
        # ~ (Status.submitted, 'submitted'),
        # ~ (Status.processing, 'processing'),
        # ~ (Status.completed, 'completed'),
        # ~ (Status.suspended, 'suspended'),
        # ~ (Status.declined, 'declined'),
    # ~ ]

    '''
    status = models.CharField(max_length=10, 
        choices=status_list,
        default=Status.submitted,
    )
    '''
    
    @transition(field=status, source=['submitted', 'suspended'],
        target='processing'
    )
    def submit(self):
        pass
    
    @transition(field=status, source='processing', target='suspended')
    def suspend(self):
        pass
    
    @transition(field=status, source='processing', target='completed')
    def complete(self):
        pass
    
    @transition(field=status, source=['processing', 'suspended'],
        target='declined'
    )
    def decline(self):
        pass

    @classmethod
    def create_payment(cls, user, order):
        new_payment = cls(user)
        new_payment.order = order
        new_payment.paymentsystem = paymentsystem
        new_payment.billAmount = order.order_cost
        new_payment.save()
        return new_payment


    class PaymentSystem:
        portmone = 'portmone'
        cash = 'cash'
    
    paymentsystem_list = [
        (PaymentSystem.portmone, 'portmone'),
        (PaymentSystem.cash, 'cash'),
    ]

    class Meta:
        verbose_name_plural = 'Payments'
    '''     
    @classmethod
    def create_payment(cls, user, paymentsystem, sum, order)
        pass
    ''' 
    def __str__(self):
        return 'user {} has payed for order {}'.format(self.user, self.order)


class PaymentSystemLog(models.Model):
    #data sent to payments_system
    shopOrderNumber = models.ForeignKey('orders.Order', 
        on_delete=models.PROTECT, null=True, blank=False
    )
    payeeId = models.IntegerField(null=True, blank=False)
    dt = models.DateTimeField(auto_now=True) #sent_at
    billAmount = models.FloatField(null=True, blank=False)
    raw_data = JSONField()

    #response from payments_system
    SHOPBILLID = models.IntegerField(null=True, blank=False)
    SHOPORDERNUMBER = models.CharField(max_length=50, null=True, blank=False)
    BILL_AMOUNT = models.FloatField(null=True, blank=False)
    RESULT = models.SmallIntegerField(null=True, blank=False)
    raw_response = JSONField()

    def __str__(self):
        return 'order {} is prossed {}'.format(self.order, self.processed_ok)

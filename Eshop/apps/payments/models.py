from django.db import models
from django.contrib.postgres.fields import JSONField
from django_fsm import FSMField, transition

paymentsystem_list = [
        ('portmone', 'portmone'),
        ('cash', 'cash'),
]


class Payments(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    order = models.ForeignKey('orders.Order', on_delete=models.PROTECT)
    paymentsystem = models.CharField(max_length=10, 
        choices=paymentsystem_list, default='portmone'
    )
    billAmount = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add=True)
    
    '''
     /order/<order_id>/pay
     class PayOrder(generic.CreateView):
        def create(self)
            order = get_object_or_404(Order, pk=self.kwargs.order_id)
            paymentsystem = self.request.json['paymentsystem']
            order.paymentsystem = paymentsystem
            payment = Payment.create_payment(
                user=self.request.user, 
                order=order,
                paymentsystem=paymentsystem
            )
                
    '''
    @classmethod
    def create_payment(cls, user, order, paymentsystem):
        new_payment = cls(user)
        new_payment.order = order
        new_payment.paymentsystem = paymentsystem
        new_payment.billAmount = order.order_cost
        new_payment.save()
        return new_payment

    
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

    '''
    status = models.CharField(max_length=10, 
        choices=status_list,
        default=Status.submitted,
    )
    '''

    status = FSMField(default=status_list[0], choices=status_list)

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
        on_delete=models.PROTECT
    )
    payeeId = models.IntegerField()
    dt = models.DateTimeField(auto_now=True) #sent_at
    billAmount = models.FloatField()
    raw_data = JSONField()

    #response from payments_system
    SHOPBILLID = models.IntegerField()
    SHOPORDERNUMBER = models.CharField(max_length=50)
    BILL_AMOUNT = models.FloatField()
    RESULT = models.SmallIntegerField()
    raw_response = JSONField()

    def __str__(self):
        return 'order {} is prossed {}'.format(self.order, self.processed_ok)

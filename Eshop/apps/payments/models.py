from django.db import models
from django.contrib.postgres.fields import JSONField
from django_fsm import FSMField, transition


class Payments(models.Model):
	payment_date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
	order = models.ForeignKey('orders.Order', on_delete=models.PROTECT)
	paymentsystem = models.CharField(max_length=50)
	#TODO: payment_sum
	
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
	order = models.ForeignKey('orders.Order', on_delete=models.PROTECT)
	
	#data sent to payments_system
	raw_data = JSONField()
	payer_id = models.CharField(max_length=50)
	sent_at = models.DateTimeField(auto_now=True)

	#response from payments_system	
	raw_response = JSONField()
	receiver_id = models.CharField(max_length=50)
	processed_at = models.DateTimeField(auto_now=True)

	processed_ok = models.BooleanField(default=True)

	def __str__(self):
		return 'order {} is prossed {}'.format(self.order, self.processed_ok)

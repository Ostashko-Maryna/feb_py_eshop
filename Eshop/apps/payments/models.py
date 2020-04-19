from django.db import models
# ~ from apps.wallets import Wallet
# ~ from apps.user_profiles import User
# ~ from apps.orders import Order

class Payments(models.Model):
	payment_date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
	order = models.ForeignKey('orders.Order', on_delete=models.PROTECT)
	paysystem = models.CharField(max_length=50)
	
	
	class Status:
		submitted = 'submitted'
		completed = 'completed'
		suspended = 'suspended'		
		declined = 'declined'
	
	status_list = [
        (Status.submitted, 'submitted'),
        (Status.completed, 'completed'),
        (Status.suspended, 'suspended'),
        (Status.declined, 'declined'),
    ]
	
	status = models.CharField(max_length=10, 
		choices=status_list,
		default=Status.submitted,
	)

	class PaymentSystem:
		portmone = 'portmone'
		cash = 'cash'
	
	paymentsystem_list = [
		(PaymentSystem.portmone, 'portmone'),
		(PaymentSystem.cash, 'cash'),
	]

	class Meta:
		verbose_name_plural = 'Payments'
	
	def __str__(self):
		return 'user {} has payed for order {}'.format(self.user, self.order)


class PaymentSystemLog(models.Model):
	order = models.ForeignKey('orders.Order', on_delete=models.PROTECT)
	
	#data sent to payments_system
	raw_data = models.TextField()
	sent_at = models.DateTimeField(auto_now=True)

	#response from payments_system	
	raw_response = models.TextField()
	processed_at = models.DateTimeField(auto_now=True)

	processed_ok = models.BooleanField(default=True)

	def __str__(self):
		return 'order {} is prossed {}'.format(self.order, self.processed_ok)

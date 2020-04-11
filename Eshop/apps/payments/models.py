from django.db import models
# ~ from apps.wallets import Wallet
# ~ from apps.user_profiles import User
# ~ from apps.orders import Order

class Payments(models.Model):
	payment_date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey('user_profiles.User', on_delete=models.PROTECT)
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

	class PaySystem:
		portmone = 'portmone'
		wallet = 'wallet'
		cash = 'cash'
	
	paysystem_list = [
		(PaySystem.portmone, 'portmone'),
		(PaySystem.wallet, 'wallet'),
		(PaySystem.cash, 'cash'),
	]
	
	def __str__(self):
		return 'user {} has payed for order {}'.format(self.user, self.order)

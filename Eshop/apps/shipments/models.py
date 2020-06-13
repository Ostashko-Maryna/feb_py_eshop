import uuid
import datetime
from django.db import models
from django.utils import timezone

class Options:
		PICK_UP = 'PICK_UP'
		COURIER = 'COURIER'
		NOVA_POSHTA = 'NOVA_POSHTA'

		shipment_options = [
			(PICK_UP, 'Pick up'),
			(COURIER, 'Courier'),
			(NOVA_POSHTA,'Nova Poshta'),
			]
		
		PACKING='PACKING'
		PICKED_UP='PICKED_UP'
		ON_THE_WAY='ON_THE_WAY'
		DELIVERED='DELIVERED'

		shipment_status_options=[
		(PACKING,'Packing'),
		(PICKED_UP, 'Picked up by courier'),
		(ON_THE_WAY, 'On the way'),
		(DELIVERED,'Delivered'),
		]


class Shipment(models.Model):
	
	order = models.OneToOneField('orders.Order', on_delete = models.CASCADE,
		related_name = 'order', blank = True, null = True)
	shipment_id = models.UUIDField(default=uuid.uuid4, editable=False)
	shipment_status_date_created = models.DateTimeField(auto_now_add = True)
	shipment_status_date_updated = models.DateTimeField(auto_now = True)
	shipment_address_region = models.CharField(max_length = 50, null = True)
	shipment_address_city = models.CharField(max_length = 50)
	shipment_adress_street = models.CharField(max_length = 50)
	shipment_adress_house = models.CharField(max_length = 10)
	shipment_adress_apartment = models.PositiveSmallIntegerField(null = True, blank = True)
	shipment_comment = models.TextField(blank = True)

	

	shipment_type = models.CharField(max_length=20,
										 default = Options.PICK_UP, 
										 choices= Options.shipment_options)

	shipment_status_type = models.CharField(max_length=50, 
												default = Options.PACKING,
												choices= Options.shipment_status_options)

	def permissions(self, user):
		if self.order.user == user:
			if self.shipment_status_type == Options.PACKING:
				return ['can delete', 'can edit', 'can create']
			else:
				return ['can create']
		else:
			return []

	def __str__(self):
		return 'Order №{}'.format(self.shipment_id)

from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from .models import Shipment, Options

class ShipmentPermission(BasePermission):
	def has_permission(self,request,view):
		obj = get_object_or_404(Shipment, 
			pk=view.kwargs.get('shipment_id'),
			order__user=view.request.user)
		if request.method != 'GET':
			return obj.shipment_status_type == Options.PACKING
		return obj
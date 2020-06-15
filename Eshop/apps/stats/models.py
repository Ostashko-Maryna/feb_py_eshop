from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone
import datetime


class Stats(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    action_date = models.DateTimeField(auto_now_add=True)
    data = JSONField()

    @property
    def action(self):
        return self.data['Action']

    @property
    def last_view_product(self):
        if self.data['Action'] == 'View':
            return self.action_date >= timezone.now() - datetime.timedelta(days=1)
        else:
            pass

    @property
    def last_buy_product(self):
        if self.data['Action'] == 'Buy':
            return '{} sold for {} UAH'.format(self.data['Product'], self.data['Sales Price']*  self.data['Sales Amount'])
        else:
            pass

    '''
    class Action:
        view = 'View'
        buy = 'Buy'
        add_to_cart = 'Add_to_cart'

    action_list = [
        (Action.view, 'View'),
        (Action.buy, 'Buy'),
        (Action.add_to_cart,'Add to cart'),
        ]
    variants = models.CharField(max_length=20, default=Action.view, choices=action_list)
    
    data = JSONField() example 
    action.buy = {"Product": "Product_2", "Sales Price": 134, "Sales Amount": 23, "Total sales":"3082"}
    action.view = {"Product": "Product_1"}
    action.add_to_cart = {"Product": "Product_3", "cart_id": "10", "Sales Price": 1345, "Sales Amount": 25}
    '''
from django.contrib.postgres.fields import JSONField
from django.db import models


class Stats(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    action_date = models.DateTimeField(auto_now_add=True)

    class Action:
        view = 'View'
        buy = 'buy'
        add_to_cart = 'add_to_cart'

    action_list = [
        (Action.view, 'View'),
        (Action.buy, 'Buy'),
        (Action.add_to_cart,'Add to cart'),
        ]
    variants = models.CharField(max_length=20, default=Action.view, choices=action_list)

    data = JSONField()

    '''
    data = JSONField() example 
    
    action.buy = {"Product": "Product_2", "Sales Price": 134, "Sales Amount": 23, "Total sales":"3082"}
    action.view = {"Product": "Product_1"}
    action.add_to_cart = {"Product": "Product_3", "cart_id": "10", "Sales Price": 1345, "Sales Amount": 25}
    
    
    '''



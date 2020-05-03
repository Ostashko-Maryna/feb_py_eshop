from django.contrib import admin
from apps.carts.models import Cart, CartItem
from django.contrib.auth import get_user_model
User = get_user_model()


class CartAdmin(admin.ModelAdmin):

    class Meta:
        model = Cart


    fieldsets = [('Опис', {'fields': ['user',  ]}),]         
    list_display = ['id', 'user', 'not_empty', 'created', 'updated', 
                  'total_price', 'cart_list', 'not_available']
    readonly_fields = ['id', 'created', 'updated',]
    # list_editable = ['cart_list', 'not_available']
class CartItemAdmin(admin.ModelAdmin):

    class Meta:
        model = CartItem



    fieldsets = [('Опис',  {'fields': [ 'product', 'quantity', 'cart',]}),]
    list_display = ['id', 'user', 'product', 
                    'quantity', 'cart', 'cart_item_status']
    readonly_fields = ['user',]
    list_editable = ['quantity']
    
    
admin.site.unregister(Cart)
admin.site.register(Cart, CartAdmin)
admin.site.unregister(CartItem)
admin.site.register(CartItem, CartItemAdmin)


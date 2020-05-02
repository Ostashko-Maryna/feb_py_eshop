from django.contrib import admin
from apps.carts.models import Cart, CartItem
from django.contrib.auth import get_user_model
User = get_user_model()


class CartAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Cart
        
    fieldsets = [('Опис', {'fields': ['customer', 'created', 'updated', 'cart_list', 'not_available']}),]         
    list_display = ['id', 'customer', 'not_empty', 'created', 'updated', 
                  'total_price', 'cart_list', 'not_available']
    readonly_fields = ['created', 'updated',]
    # list_editable = ['cart_list', 'not_available']
class CartItemAdmin(admin.ModelAdmin):
    
    class Meta:
        model = CartItem
        
    fieldsets = [('Опис',  {'fields': [ 'product', 'quantity', 'cart',]}),]
    list_display = ['id', 'customer', 'product', 
                    'quantity', 'cart', 'cart_item_status']
    readonly_fields = ['customer',]
    list_editable = ['quantity']
    
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)


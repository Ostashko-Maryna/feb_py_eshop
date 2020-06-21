from django.contrib import admin
from apps.carts.models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):

    class Meta:
        model = Cart

    fieldsets = [('Опис', {'fields': ['user', ]}),]         
    list_display = ['id', 'cart_user_name', 'cart_number', 'not_empty', 
                    'created_on', 'updated_on', 'created_by', 
                  'total_price', 'cart_list', 'not_available']


class CartItemAdmin(admin.ModelAdmin):

    class Meta:
        model = CartItem

    fieldsets = [('Опис',  {'fields': ['product', 'quantity', 'cart', ]}),]
    list_display = ['id',  'created_by', 'cart', 'product', 'quantity', 
                    'created_on', 'updated_on', 'created_by', 
                    'cart_item_status', 'counter']
    readonly_fields = ['user', 'counter']
    list_editable = ['quantity']


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
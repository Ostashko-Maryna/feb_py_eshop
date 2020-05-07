from django.contrib import admin
from apps.carts.models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):

    class Meta:
        model = Cart

    fieldsets = [('Опис', {'fields': ['customer',  ]}),]         
    list_display = ['id', 'customer', 'not_empty', 'created', 'updated', 
                  'total_price', 'cart_list', 'not_available']

class CartItemAdmin(admin.ModelAdmin):

    class Meta:
        model = CartItem

    fieldsets = [('Опис',  {'fields': ['product', 'stock_count', 'quantity', 'cart',]}),]
    list_display = ['id', 'customer', 'cart', 'product', 'quantity', 'cart_item_status', 'stock_count']
    readonly_fields = ['customer', 'stock_count',]
    list_editable = ['quantity']


admin.site.unregister(Cart)
admin.site.register(Cart, CartAdmin)
admin.site.unregister(CartItem)
admin.site.register(CartItem, CartItemAdmin)


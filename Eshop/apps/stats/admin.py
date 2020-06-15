from django.contrib import admin
from .models import Stats


class StatsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'action_date', 'action', 'data', 'last_view_product', 'last_buy_product']
    list_filter = ['user', 'action_date']
    search_fields = ['user__username', 'action_date']
    date_hierarchy = 'action_date'


admin.site.register(Stats, StatsAdmin)

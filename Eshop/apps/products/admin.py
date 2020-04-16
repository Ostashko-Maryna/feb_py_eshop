from django.contrib import admin
from .models import Product, Review, Kit


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Артикул та Назва',                   {'fields': ['vendor_code', 'name']}),
        ('Ціна та Наявність',                  {'fields': ['price', 'stock_count']}),
        ('Опис',                               {'fields': ['description']}),
        ('Характеристики',                     {'fields': ['characteristics']}),
        ('Дані щодо Створення та Доступності', {'fields': ['created_by', 'created_at', 'available']}),
    ]
    inlines = [ReviewInline]
    list_display = ['id', 'vendor_code', 'name', 'price', 'stock_count', 'description',
                    'characteristics', 'available', 'created_by', 'created_at', 'updated_at']
    list_filter = ['available', 'created_by', 'created_at', 'updated_at']
    list_editable = ['price', 'stock_count', 'available']
    search_fields = ['vendor_code', 'name', 'description', 'characteristics']
    date_hierarchy = 'created_at'


class KitAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Kit, KitAdmin)

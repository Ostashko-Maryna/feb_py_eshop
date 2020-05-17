from django.contrib import admin
from .models import Product, Review, Kit


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    verbose_name_plural = 'Відгуки'


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Артикул та Назва',  {'fields': ['vendor_code', 'name']}),
        ('Ціна та Наявність', {'fields': ['price', 'stock_count']}),
        ('Опис',              {'fields': ['description']}),
        ('Характеристики',    {'fields': ['characteristics']}),
        ('Доступність',       {'fields': ['available']}),
    ]
    inlines = [ReviewInline]
    list_display = ['id', 'vendor_code', 'name', 'price', 'stock_count', 'description',
                    'characteristics', 'available', 'created_by', 'created_at', 'updated_at']
    list_filter = ['available', 'created_by', 'created_at', 'updated_at']
    list_editable = ['price', 'stock_count', 'available']
    search_fields = ['vendor_code', 'name', 'description', 'characteristics']
    date_hierarchy = 'created_at'


class ReviewAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Продукт',     {'fields': ['product']}),
        ('Відгук',      {'fields': ['review']}),
        ('Доступність', {'fields': ['available']}),
    ]
    list_display = ['id', 'product', 'user', 'review', 'available', 'created_at']
    list_filter = ['available', 'product', 'user', 'created_at']
    list_editable = ['available']
    search_fields = ['review']
    date_hierarchy = 'created_at'
    raw_id_fields = ['product']


class KitAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Продукти',    {'fields': ['products']}),
        ('Опис',        {'fields': ['description']}),
        ('Термін до',   {'fields': ['term']}),
        ('Доступність', {'fields': ['available']}),
    ]
    list_display = ['id', 'description', 'available', 'term',
                    'created_by', 'created_at', 'updated_at']
    list_filter = ['available', 'term', 'created_by', 'created_at', 'updated_at']
    search_fields = ['description']
    list_editable = ['available', 'term']
    date_hierarchy = 'created_at'
    raw_id_fields = ['products']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Kit, KitAdmin)

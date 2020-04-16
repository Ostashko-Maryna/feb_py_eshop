from django.contrib import admin

from .models import Gallery


class GalleryAdmin(admin.ModelAdmin):
	raw_id_fields = ["product"]

admin.site.register(Gallery, GalleryAdmin)

class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 3

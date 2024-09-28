from django.contrib import admin
from .models import Property, Category

# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Property, PropertyAdmin)
admin.site.register(Category, CategoryAdmin)
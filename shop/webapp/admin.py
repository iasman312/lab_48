from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price']
    list_filter = ['name']
    search_fields = ['name', 'category']
    fields = ['name', 'description', 'category', 'bonus', 'price']
    readonly_fields = ['id']


admin.site.register(Product, ProductAdmin)

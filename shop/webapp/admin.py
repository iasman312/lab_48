from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price']
    list_filter = ['name']
    search_fields = ['name', 'category']
    fields = ['name', 'description', 'category', 'balance', 'price']
    readonly_fields = ['id']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)

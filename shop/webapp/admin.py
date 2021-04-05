from django.contrib import admin
from .models import Product, Category, Cart, Order, ProductOrder


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price']
    list_filter = ['name']
    search_fields = ['name', 'category']
    fields = ['name', 'description', 'category', 'balance', 'price']
    readonly_fields = ['id']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'tel_number', 'created_at']
    ordering = ('-created_at',)


class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'order', 'quantity']



admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductOrder, ProductOrderAdmin)

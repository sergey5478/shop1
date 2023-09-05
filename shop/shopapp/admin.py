from django.contrib import admin
from .models import Client, Product, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    ordering = ['name', '-email']
    fields = ['name', 'phone_number', 'email', 'client_address', 'customer_registration_date']
    readonly_fields = ['name', 'email', 'customer_registration_date']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name_product', 'product_description']
    ordering = ['name_product', '-product_description']
    fields = ['name_product', 'price_product', 'product_description', 'quantity_product', 'date_product_added', 'image']
    readonly_fields = ['name_product', 'image', 'date_product_added']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_client', 'order_product']
    ordering = ['order_client', '-order_product']
    fields = ['order_client', 'total_amount_order', 'order_product', 'date_order']
    readonly_fields = ['order_client', 'order_product', 'date_order']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

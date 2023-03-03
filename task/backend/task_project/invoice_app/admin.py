from django.contrib import admin
from .models import Invoice , Products


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'invoice_number', 'total_cost']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_price', 'product_quantity', 'product_total_cost', 'invoice']
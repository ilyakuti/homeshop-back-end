from django.contrib import admin
from .models import Product

# Register your models here.

class Productadmin (admin.ModelAdmin):
    list_display = ["short_name_product", "price_product", "in_stock", "color_product"]
    list_editable = ["price_product", "in_stock"]
    search_fields = ["short_name_product"]

admin.site.register (Product, Productadmin)
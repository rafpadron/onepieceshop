from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'description', 'price', 'stock')
    search_fields = ('name', 'description')
    list_filter = ('stock',)

admin.site.register(Product, ProductAdmin)
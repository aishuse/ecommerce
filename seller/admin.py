from django.contrib import admin
from seller.models import ProductStock, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'price', 'category', 'stock', 'user'
    ]
    list_filter = ('name', 'user', 'category')


class ProductStockAdmin(admin.ModelAdmin):
    list_display = [
        'product', 'stock_available', 'user'
    ]
    list_filter = ('product', 'stock_available', 'user')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductStock, ProductStockAdmin)
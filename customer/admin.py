
from django.contrib import admin
from customer.models import Cart, Address, Purchase


class PurchaseAdmin(admin.ModelAdmin):
    list_display = [
         'item', 'quantity', 'user', 'seller', 'status', 'created_date'
    ]
    list_filter = ('item', 'seller', 'status')


class CartAdmin(admin.ModelAdmin):
    list_display = [
         'item', 'quantity', 'user', 'status'
    ]
    list_filter = ('item', 'quantity', 'user')


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'pin', 'user'
    ]
    list_filter = ('name', 'pin', 'user')



admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Address, AddressAdmin)



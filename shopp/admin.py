from django.contrib import admin
from .models import Shop, Guard, Seller, Buyer, Product


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location']

@admin.register(Guard)
class GuardAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'phone', 'position']

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'phone', 'position']

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'phone', 'gender']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'price', 'description', 'quantity']

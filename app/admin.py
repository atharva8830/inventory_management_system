from django.contrib import admin
from .models import Category, Supplier, Product , InventoryTransaction


class proadmin(admin.ModelAdmin):
    list_display = ['id','name', 'category', 'supplier', 'price', 'quantity', 'description', 'created_at', 'updated_at',]
    
class catadmin(admin.ModelAdmin):

    list_display = ['name', 'description',]

class supadmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'created_at', ]

class InventoryTransactionadmin(admin.ModelAdmin) :
    list_display = ['id', 'product', 'supplier', 'transaction_type', 'quantity', 'created_at',]


admin.site.register(Category , catadmin)
admin.site.register(Product, proadmin)
admin.site.register(Supplier, supadmin)
admin.site.register(InventoryTransaction , InventoryTransactionadmin)
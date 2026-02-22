from django.contrib import admin
from .models import Category, Supplier, Product


class proadmin(admin.ModelAdmin):
    list_display = ['id','name', 'category', 'supplier', 'price', 'quantity', 'description', 'created_at', 'updated_at',]
    
class catadmin(admin.ModelAdmin):

    list_display = ['name', 'description',]

class supadmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'created_at', ]

admin.site.register(Category , catadmin)
admin.site.register(Product, proadmin)
admin.site.register(Supplier)
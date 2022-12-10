from django.contrib import admin
from .models import Category, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'image', 'category', 'created', 'updated']
    list_editable = ['description', 'price', 'image']
    list_per_page = 10

admin.site.register(Product, ProductAdmin)
from django.contrib import admin
from .models import Category, SubCategory, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(SubCategory, SubCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'image', 'category', 'subcategory','created', 'updated']
    list_editable = ['description', 'price', 'image']
    list_per_page = 10

admin.site.register(Product, ProductAdmin)

from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.
def prod_list(request, category_id=None):
    category = None
    products = Product.objects
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category)
    return render(request, 'shop.html', {'category':category, 'products':products})
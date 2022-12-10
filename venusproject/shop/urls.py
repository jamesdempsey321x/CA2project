from django.urls import path
from .views import prod_list, prod_details
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.prod_list, name = 'all_prod_list'),
    path('<uuid:category_id>/', views.prod_list, name = 'products_by_category'),
    path('<uuid:category_id>/<uuid:product_id>/', views.prod_details, name = 'products_details'),
]

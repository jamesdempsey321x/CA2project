from django.urls import path
from .views import prod_list
from . import views

urlpatterns = [
    path('', views.prod_list, name = 'shop'),
]

from django.shortcuts import render
from django.views.generic import ListView
from .models import Involve

# Create your views here.
class InvolveListView(ListView):
    model = Involve
    template_name = 'involve.html'
    context_object_name = "all_involve_list"
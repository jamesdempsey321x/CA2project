from django.shortcuts import render
from django.views.generic import ListView
from .models import News

# Create your views here.
class NewsListView(ListView):
    paginate_by = 12
    model = News
    template_name = 'news.html'
    context_object_name = "all_news_list"

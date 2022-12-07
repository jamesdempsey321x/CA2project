from django.urls import path
from .views import InvolveListView

urlpatterns = [
    path('', InvolveListView.as_view(), name ='involve_list'),

]
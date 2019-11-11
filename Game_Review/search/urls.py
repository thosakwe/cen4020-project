from django.urls import path, re_path
from .views import search
from .views import index
from . import views

urlpatterns = [
    path('search/', search, name='search'),
    path('index/', index, name='index'),
]
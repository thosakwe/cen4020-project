from django.urls import path, re_path
from .views import search
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='review-home'),
    path('about/', views.about, name='review-about'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/<int:id>/', views.profile, name='profile'),
]
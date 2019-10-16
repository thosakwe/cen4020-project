from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.get_by_id, name='new'),
    path('new/', views.new, name='new'),
]
from django.urls import path, re_path
from .views import guidebook_detail, GuidebookCreateView, GuidebookUpdateView, GuidebookDeleteView
from . import views
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('guidebook/<int:pk>/',guidebook_detail, name="guidebook-detail"),
    path('guidebook/new/<int:game>/', GuidebookCreateView.as_view(), name="guidebook-create"),
    path('guidebook/<int:pk>/update/', GuidebookUpdateView.as_view(), name="guidebook-update"),
    path('guidebook/<int:pk>/delete/', GuidebookDeleteView.as_view(), name="guidebook-delete"),
]
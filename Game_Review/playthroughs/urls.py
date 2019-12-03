from django.urls import path, re_path
from .views import PlaythroughListView, playthrough_detail, PlaythroughCreateView, PlaythroughUpdateView, PlaythroughDeleteView
from . import views
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='playthrough-home'),
    path('playthroughs/<int:pk>/',playthrough_detail, name="playthrough-detail"),
    path('playthroughs/new/<int:game>/', PlaythroughCreateView.as_view(), name="playthrough-create"),
    path('playthroughs/<int:pk>/update/', PlaythroughUpdateView.as_view(), name="playthrough-update"),
    path('playthroughs/<int:pk>/delete/', PlaythroughDeleteView.as_view(), name="playthrough-delete"),
    path('nes/', views.news, name='playthrough-news'),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    #url('', include('social.apps.django_app.urls', namespace='social')),
    #url(r'^upload/', include('upload.urls')),
    #url(r'^growth/', include('growth.urls')),
]
from django.urls import path, re_path
from .views import PlaythroughListView, PlaythroughDetailView, PlaythroughCreateView, PlaythroughUpdateView, PlaythroughDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='playthrough-home'),
    path('playthroughs/<int:pk>/',PlaythroughDetailView.as_view(), name="playthrough-detail"),
    #path('review/new/', ReviewCreateView.as_view(), name="review-create"),
    #path('review/new/(?P<game>\d+)/$', ReviewCreateView.as_view(), name="review-create"),
    re_path('^playthroughs/new/(?P<game>[0-9]+)/$', PlaythroughCreateView.as_view(), name="playthrough-create"),
    path('playthroughs/<int:pk>/update/', PlaythroughUpdateView.as_view(), name="playthrough-update"),
    path('playthroughs/<int:pk>/delete/', PlaythroughDeleteView.as_view(), name="playthrough-delete"),
    path('about/', views.about, name='playthrough-about'),
]
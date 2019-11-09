from django.urls import path, re_path
from .views import ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='review-home'),
    path('review/<int:pk>/',ReviewDetailView.as_view(), name="review-detail"),
    #path('review/new/', ReviewCreateView.as_view(), name="review-create"),
    #path('review/new/(?P<game>\d+)/$', ReviewCreateView.as_view(), name="review-create"),
    #re_path('^review/new/(?P<game>[0-9]+)/$', ReviewCreateView.as_view(), name="review-create"),
    path('review/new/<int:game>/', ReviewCreateView.as_view(), name="review-create"),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name="review-update"),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name="review-delete"),
    path('about/', views.about, name='review-about'),
]
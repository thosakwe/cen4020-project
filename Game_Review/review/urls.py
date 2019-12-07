from django.urls import path, re_path
from .views import ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='review-home'),
    path('review/<int:pk>/', views.review_detail, name="review-detail"),
    path('review/new/<int:game>/', ReviewCreateView.as_view(), name="review-create"),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name="review-update"),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name="review-delete"),
    path('news/', views.news, name='review-news'),
    path('banned/', views.news, name='review-banned'),
    path('duplicate/', views.news, name='review-duplicate'),
]
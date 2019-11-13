from django.shortcuts import render
from .models import Review
from game.models import Game
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Review
from users.models import Profile
import re
import collections

# Create your views here.
def home(request):
    lst =[1,2,3,4]
    games = Game.objects.all()
    for game in games:
        path = game.image_path.url
        game.image_path = re.sub(r'^review', '', path)
    context = {'games': games,'list':lst}
    return render(request, 'review/home.html', context)

def news(request):
    games = Game.objects.all()
    review = Review.objects.order_by('-score')
    return render(request, 'review/news.html',{'games':games,'review':review})

class ReviewListView(ListView):
    """
    This view has not been implemented yet, but reviews get listed
    on the game page anyway
    """
    model = Review
    template_name = "review/review.html"
    context_object_name = 'review'
    ordering = ['date_posted']

class ReviewDetailView(DetailView):
    model = Review
    template_name = "review/review_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        return context


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['title','content']

    def form_valid(self, form):
        game = Game.objects.get(pk=self.kwargs['game'])
        form.instance.author = self.request.user
        form.instance.game = game
        form.instance.score = 3
        return super().form_valid(form)

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.score = 3
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        else:
            return False

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Review
    success_url = '/'
    template_name = "review/review_delete.html"
    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        else:
            return False
# def home(request):
#     context = {
#         'reviews': Review.objects.all()
#     }
#     return render(request, 'review/home.html', context)

# def about(request):
#     return render(request, 'review/about.html', {'title':'About'})
from django.shortcuts import render, get_object_or_404
from .models import Review, Comment, ReviewVote, CommentVote
from game.models import Game
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from users.models import Profile
from users.forms import enforce_rate_limit
from .forms import CommentForm
from .models import Review
import re
import collections
from django.db import models
import json

# Create your views here.
def home(request):
    games = Game.objects.filter(coming_soon=False)
    for game in games:
        path = game.image_path.url
        game.image_path = re.sub(r'^review', '', path)
    context = {'games': games}
    return render(request, 'review/home.html', context)

def coming_soon(request):
    games = Game.objects.filter(coming_soon=True)
    for game in games:
        path = game.image_path.url
        game.image_path = re.sub(r'^review', '', path)
    context = {'games': games}
    return render(request, 'review/coming-soon.html', context)

# return three highly rated games
def news(request):
    lst = []
    dic = {}
    games = Game.objects.all()
    games = games.values_list('title',flat=True).distinct()
    review = Review.objects.order_by('-score')
    for i in review:
        if i.game not in dic:
            lst.append(i)
            dic[i.game] = 'entered'
    return render(request, 'review/news.html',{'games':games,'review':lst})

def banned(request):
    return render(request, 'review/banned.html')

def duplicate(request):
    return render(request, 'review/duplicate.html')

def too_early(request):
    return render(request, 'review/too-early.html')

class ReviewListView(ListView):
    """
    This view has not been implemented yet, but reviews get listed
    on the game page anyway
    """
    model = Review
    template_name = "review/review.html"
    context_object_name = 'review'
    ordering = ['date_posted']

def review_detail(request, pk):
    template_name = 'review/review_detail.html'
    review = get_object_or_404(Review, pk=pk)
    comments = review.comment_set.all()#.filter(active=True)
    new_comment = None
    comment_form = CommentForm()
    if request.method == 'POST':
        # Comment posted
        print(request.POST)
        if "comment_form" in request.POST:
            comment_form = CommentForm(request.POST, request.FILES)
            comment_form.initial['author'] = request.user
            comment_form.initial['review'] = review
            if comment_form.is_valid():
                new_comment = Comment()
                new_comment.review = review
                new_comment.author = request.user
                new_comment.content = comment_form.cleaned_data['content']
                new_comment.save()
        
        # Liked review
        user_vote = ReviewVote.objects.filter(user=request.user,review=review)
        if "like_btn" in request.POST:
            if not user_vote.filter(vote=1):
                new_like = ReviewVote()
                new_like.review = review
                new_like.user = request.user
                new_like.vote = 1
                new_like.save()
            else:
                user_vote.delete()
            if user_vote.filter(vote=-1).exists():
                user_vote.get(vote=-1).delete()

        # Disliked review
        if "dislike_btn" in request.POST:
            if not user_vote.filter(vote=-1):
                new_like = ReviewVote()
                new_like.review = review
                new_like.user = request.user
                new_like.vote = -1
                new_like.save()
            else:
                user_vote.delete()
            if user_vote.filter(vote=1).exists():
                user_vote.get(vote=1).delete()

        # Liked review
        if "clike_btn" in request.POST:
            comment = get_object_or_404(Comment, pk=int(request.POST['clike_btn']))
            user_vote = CommentVote.objects.filter(user=request.user,comment=comment)
            if not user_vote.filter(vote=1):
                new_like = CommentVote()
                new_like.comment = comment
                new_like.user = request.user
                new_like.vote = 1
                new_like.save()
            else:
                user_vote.delete()
            if user_vote.filter(vote=-1).exists():
                user_vote.get(vote=-1).delete()

        # Disliked review
        if "cdislike_btn" in request.POST:
            comment = get_object_or_404(Comment, pk=int(request.POST['cdislike_btn']))
            user_vote = CommentVote.objects.filter(user=request.user,comment=comment)
            if not user_vote.filter(vote=-1):
                new_like = CommentVote()
                new_like.comment = comment
                new_like.user = request.user
                new_like.vote = -1
                new_like.save()
            else:
                user_vote.delete()
            if user_vote.filter(vote=1).exists():
                user_vote.get(vote=1).delete()
    context = {
            'review': review,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form,
        }
    return render(request, template_name, context)

class ReviewDetailView(DetailView):
    model = Review
    template_name = "review/review_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['title','content']

    def post(self, *args, **kwargs):
        game = Game.objects.get(pk=self.kwargs['game'])
        if game.coming_soon:
            return HttpResponseRedirect("/too-early")
        rate_limit_result = enforce_rate_limit(self.request, game, self.request.user, Review)
        if rate_limit_result:
            return HttpResponseRedirect("/banned")
        elif rate_limit_result == False:
            return HttpResponseRedirect("/duplicate")
        else:
            return super(ReviewCreateView, self).post(*args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(ReviewCreateView, self).get_context_data(**kwargs)
        ctx['game'] = Game.objects.get(pk=self.kwargs['game'])
        return ctx

    def form_valid(self, form):
        print(self.kwargs)
        game = Game.objects.get(pk=self.kwargs['game'])
        form.instance.author = self.request.user
        form.instance.game = game
        form.instance.score = int(form.data.get('score'))
        return super().form_valid(form)

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.score = int(form.data.get('score'))
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
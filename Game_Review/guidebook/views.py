from django.shortcuts import render, get_object_or_404
from .models import Guidebook, GuidebookComment, GuidebookVote, GuidebookCommentVote
from django.http import HttpResponseRedirect

from game.models import Game
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from review.forms import CommentForm

# Create your views here.
def guidebook_detail(request,pk):
    template_name = "guidebook/guidebook_detail.html"
    guidebook = get_object_or_404(Guidebook, pk=pk)
    comments = guidebook.guidebookcomment_set.all()#.filter(active=True)
    new_comment = None
    comment_form = CommentForm()
    if request.method == 'POST':
        # GuidebookComment posted
        print(request.POST)
        if "comment_form" in request.POST:
            comment_form = CommentForm(request.POST, request.FILES)
            comment_form.initial['author'] = request.user
            comment_form.initial['guidebook'] = guidebook
            if comment_form.is_valid():
                new_comment = GuidebookComment()
                new_comment.guidebook = guidebook
                new_comment.author = request.user
                new_comment.content = comment_form.cleaned_data['content']
                new_comment.save()
        
        # Liked guidebook
        user_vote = GuidebookVote.objects.filter(user=request.user,guidebook=guidebook)
        if "like_btn" in request.POST:
            if not user_vote.filter(vote=1):
                new_like = GuidebookVote()
                new_like.guidebook = guidebook
                new_like.user = request.user
                new_like.vote = 1
                new_like.save()
            else:
                user_vote.delete()
            if user_vote.filter(vote=-1).exists():
                user_vote.get(vote=-1).delete()

        # Disliked guidebook
        if "dislike_btn" in request.POST:
            if not user_vote.filter(vote=-1):
                new_like = GuidebookVote()
                new_like.guidebook = guidebook
                new_like.user = request.user
                new_like.vote = -1
                new_like.save()
            else:
                user_vote.delete()
            if user_vote.filter(vote=1).exists():
                user_vote.get(vote=1).delete()

        # Liked guidebook
        if "clike_btn" in request.POST:
            comment = get_object_or_404(GuidebookComment, pk=int(request.POST['clike_btn']))
            user_vote = GuidebookCommentVote.objects.filter(user=request.user,comment=comment)
            if not user_vote.filter(vote=1):
                new_like = GuidebookCommentVote()
                new_like.comment = comment
                new_like.user = request.user
                new_like.vote = 1
                new_like.save()
            else:
                user_vote.delete()
            if user_vote.filter(vote=-1).exists():
                user_vote.get(vote=-1).delete()

        # Disliked Guidebook
        if "cdislike_btn" in request.POST:
            comment = get_object_or_404(GuidebookComment, pk=int(request.POST['cdislike_btn']))
            user_vote = GuidebookCommentVote.objects.filter(user=request.user,comment=comment)
            if not user_vote.filter(vote=-1):
                new_like = GuidebookCommentVote()
                new_like.comment = comment
                new_like.user = request.user
                new_like.vote = -1
                new_like.save()
            else:
                user_vote.delete()
            if user_vote.filter(vote=1).exists():
                user_vote.get(vote=1).delete()
    context = {
            'object': guidebook,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form,
        }
    return render(request, template_name, context)

class GuidebookCreateView(LoginRequiredMixin, CreateView):
    model = Guidebook
    fields = ['title','content', 'pdf_file']

    def get_context_data(self, **kwargs):
        ctx = super(GuidebookCreateView, self).get_context_data(**kwargs)
        ctx['game'] = Game.objects.get(pk=self.kwargs['game'])
        return ctx

    def form_valid(self, form):
        game = Game.objects.get(pk=self.kwargs['game'])
        form.instance.author = self.request.user
        form.instance.game = game
        return super().form_valid(form)

    def form_invalid(self, form):
        print(self.kwargs)
        print(self.request.user)
        print(form.cleaned_data)
        print("form is invalid")

class GuidebookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Guidebook
    fields = ['title', 'content', 'pdf_file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        guidebook = self.get_object()
        if self.request.user == guidebook.author:
            return True
        else:
            return False

class GuidebookDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Guidebook
    success_url = '/'
    template_name = "guidebook/guidebook_delete.html"
    def test_func(self):
        guidebook = self.get_object()
        if self.request.user == guidebook.author:
            return True
        else:
            return False
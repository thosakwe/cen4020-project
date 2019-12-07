from django.shortcuts import render, get_object_or_404
from .models import playthroughs, PlaythroughComment, PlaythroughVote, PlaythroughCommentVote
from django.http import HttpResponseRedirect

from game.models import Game
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
#from .models import Video
from .forms import VideoForm
from review.forms import CommentForm
from users.forms import enforce_rate_limit 

# Create your views here.

from .models import playthroughs

# Create your views here.
def home(request):
    context = {
        'Playthroughs': playthroughs.objects.all()
    }
    return render(request, 'Playthroughs/home.html', context)
def news(request):
    return render(request, 'Playthroughs/news.html', {'title':'News'})

class PlaythroughListView(ListView):

    model = playthroughs
    template_name = "playthrough/playthrough.html"
    context_object_name = 'playthrough'
    ordering = ['date_posted']

def playthrough_detail(request,pk):
    template_name = "playthroughs/playthroughs_detail.html"
    playthrough = get_object_or_404(playthroughs, pk=pk)
    comments = playthrough.playthroughcomment_set.all()#.filter(active=True)
    new_comment = None
    comment_form = CommentForm()
    if request.method == 'POST':
        # PlaythroughComment posted
        print(request.POST)
        if "comment_form" in request.POST:
            comment_form = CommentForm(request.POST, request.FILES)
            comment_form.initial['author'] = request.user
            comment_form.initial['playthrough'] = playthrough
            if comment_form.is_valid():
                new_comment = PlaythroughComment()
                new_comment.playthrough = playthrough
                new_comment.author = request.user
                new_comment.content = comment_form.cleaned_data['content']
                new_comment.save()
        
        # Liked playthrough
        user_vote = PlaythroughVote.objects.filter(user=request.user,playthrough=playthrough)
        if "like_btn" in request.POST:
            if not user_vote.filter(vote=1):
                new_like = PlaythroughVote()
                new_like.playthrough = playthrough
                new_like.user = request.user
                new_like.vote = 1
                new_like.save()
            else:
                user_vote.delete()
            if user_vote.filter(vote=-1).exists():
                user_vote.get(vote=-1).delete()

        # Disliked playthrough
        if "dislike_btn" in request.POST:
            if not user_vote.filter(vote=-1):
                new_like = PlaythroughVote()
                new_like.playthrough = playthrough
                new_like.user = request.user
                new_like.vote = -1
                new_like.save()
            else:
                user_vote.delete()
            if user_vote.filter(vote=1).exists():
                user_vote.get(vote=1).delete()

        # Liked playthrough
        if "clike_btn" in request.POST:
            comment = get_object_or_404(PlaythroughComment, pk=int(request.POST['clike_btn']))
            user_vote = PlaythroughCommentVote.objects.filter(user=request.user,comment=comment)
            if not user_vote.filter(vote=1):
                new_like = PlaythroughCommentVote()
                new_like.comment = comment
                new_like.user = request.user
                new_like.vote = 1
                new_like.save()
            else:
                user_vote.delete()
            if user_vote.filter(vote=-1).exists():
                user_vote.get(vote=-1).delete()

        # Disliked playthrough
        if "cdislike_btn" in request.POST:
            comment = get_object_or_404(PlaythroughComment, pk=int(request.POST['cdislike_btn']))
            user_vote = PlaythroughCommentVote.objects.filter(user=request.user,comment=comment)
            if not user_vote.filter(vote=-1):
                new_like = PlaythroughCommentVote()
                new_like.comment = comment
                new_like.user = request.user
                new_like.vote = -1
                new_like.save()
            else:
                user_vote.delete()
            if user_vote.filter(vote=1).exists():
                user_vote.get(vote=1).delete()
    context = {
            'object': playthrough,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form,
        }
    return render(request, template_name, context)

class PlaythroughCreateView(LoginRequiredMixin, CreateView):
    model = playthroughs
    fields = ['title','content', 'videofile']

    def post(self, *args, **kwargs):
        game = Game.objects.get(pk=self.kwargs['game'])
        rate_limit_result = enforce_rate_limit(self.request, game, self.request.user, playthroughs)
        if rate_limit_result:
            return HttpResponseRedirect("/banned")
        elif rate_limit_result == False:
            return HttpResponseRedirect("/duplicate")
        else:
            return super(PlaythroughCreateView, self).post(*args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(PlaythroughCreateView, self).get_context_data(**kwargs)
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

class PlaythroughUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = playthroughs
    fields = ['title', 'content', 'videofile']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.score = int(form.data.get('score'))
        return super().form_valid(form)

    def test_func(self):
        playthroughs = self.get_object()
        if self.request.user == playthroughs.author:
            return True
        else:
            return False

class PlaythroughDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = playthroughs
    success_url = '/'
    template_name = "playthroughs/playthroughs_delete.html"
    def test_func(self):
        playthroughs = self.get_object()
        if self.request.user == playthroughs.author:
            return True
        else:
            return False
        
def display_video(request):
    lastvideo = playthroughs.objects.last()

    videofile = lastvideo.videofile

    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {'videofile': videofile,
               'form': form
               }

    return render(request, 'upload/videos.html', context)

from django.shortcuts import render
from .models import playthroughs
from game.models import Game
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from .models import Video
from .forms import VideoForm


# Create your views here.

from .models import playthroughs

# Create your views here.
def home(request):
    context = {
        'Playthroughs': playthroughs.objects.all()
    }
    return render(request, 'Playthroughs/home.html', context)
def about(request):
    return render(request, 'Playthroughs/about.html', {'title':'About'})

class PlaythroughListView(ListView):

    model = playthroughs
    template_name = "playthrough/playthrough.html"
    context_object_name = 'playthrough'
    ordering = ['date_posted']

class PlaythroughDetailView(DetailView):
    model = playthroughs
    template_name = "playthrough/playthrough_detail.html"

class PlaythroughCreateView(LoginRequiredMixin, CreateView):
    model = playthroughs
    fields = ['title','content']

    def form_valid(self, form):
        game = Game.objects.get(pk=self.kwargs['game'])
        form.instance.author = self.request.user
        form.instance.game_id = game.id
        form.instance.score = 3
        return super().form_valid(form)

class PlaythroughUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = playthroughs
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.score = 3
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        if self.request.user == playthroughs.author:
            return True
        else:
            return False

class PlaythroughDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = playthroughs
    success_url = '/'
    template_name = "playthrough/playthrough_delete.html"
    def test_func(self):
        playthroughs = self.get_object()
        if self.request.user == playthroughs.author:
            return True
        else:
            return False
        
def display_video(request):
    lastvideo = Video.objects.last()

    videofile = lastvideo.videofile

    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {'videofile': videofile,
               'form': form
               }

    return render(request, 'upload/videos.html', context)

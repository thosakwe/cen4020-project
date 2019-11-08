from django.shortcuts import render
from .models import Playthroughs
from game.models import Game
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

from .models import Playthroughs

# Create your views here.
def home(request):
    context = {
        'Playthroughs': Playthroughs.objects.all()
    }
    return render(request, 'Playthroughs/home.html', context)
def about(request):
    return render(request, 'Playthroughs/about.html', {'title':'About'})

class PlaythroughListView(ListView):

    model = Playthroughs
    template_name = "playthrough/playthrough.html"
    context_object_name = 'playthrough'
    ordering = ['date_posted']

class PlaythroughDetailView(DetailView):
    model = Playthroughs
    template_name = "playthrough/playthrough_detail.html"

class PlaythroughCreateView(LoginRequiredMixin, CreateView):
    model = Playthroughs
    fields = ['title','content']

    def form_valid(self, form):
        game = Game.objects.get(pk=self.kwargs['game'])
        form.instance.author = self.request.user
        form.instance.game_id = game.id
        form.instance.score = 3
        return super().form_valid(form)

class PlaythroughUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Playthroughs
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.score = 3
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        if self.request.user == Playthroughs.author:
            return True
        else:
            return False

class PlaythroughDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Playthroughs
    success_url = '/'
    template_name = "playthrough/playthrough_delete.html"
    def test_func(self):
        playthroughs = self.get_object()
        if self.request.user == playthroughs.author:
            return True
        else:
            return False
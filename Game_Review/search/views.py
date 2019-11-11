from django.shortcuts import render
from game.models import Game
import re
from .form import SearchForm


# Create your views here.
def index(request):
    return render(request, 'search/index.html', {'title': 'mukera'})

def search(request):
    name = ""
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
    lst = []
    filled = False
    games = Game.objects.all()
    for game in games:
        if game.title == name:
            lst.append(game)
        filled = True
    if name != "":
        if len(lst) == 0:
            lst.append("There is no game in that name!")
    searched = SearchForm()
    return render(request, 'search/search.html', {'searched': searched, 'result' : lst})

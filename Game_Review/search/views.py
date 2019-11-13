from django.shortcuts import render
from game.models import Game
import re
from .form import SearchForm


# Create your views here.
def search(request):
    name = ""
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
    lst = []
    filled = False
    found = True;
    games = Game.objects.all()
    for game in games:
        if game.title == name:
            lst.append(game)
        filled = True
    if name != "":
        if len(lst) == 0:
            found = False;
            lst.append("game not found!!")
    searched = SearchForm()
    return render(request, 'search/search.html', {'searched': searched, 'result' : lst, 'found' : found })

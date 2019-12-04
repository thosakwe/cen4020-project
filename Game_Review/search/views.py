from django.shortcuts import render
from game.models import Game
import re
from .form import SearchForm
from django.db.models import Q
from django.contrib.postgres.search import SearchQuery


def search(request):
    lst = []
    name = ""
    found = True
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lst = Game.objects.filter(title__icontains=name)
    searched = SearchForm()
    return render(request, 'search/search.html', {'method': request.method, 'searched': searched, 'result': lst, 'found': found})

from django.shortcuts import render

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
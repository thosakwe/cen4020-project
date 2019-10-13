from django.shortcuts import render
from .models import Review

# Create your views here.
def home(request):
    context = {
        'reviews': Review.objects.all()
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title':'About'})
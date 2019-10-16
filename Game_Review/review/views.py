from django.shortcuts import render
from .models import Review

# Create your views here.
def home(request):
    context = {
        'reviews': Review.objects.all()
    }
    return render(request, 'review/home.html', context)

def about(request):
    return render(request, 'review/about.html', {'title':'About'})

def liya(request):
    return render(request, 'review/liya.html', {'title':'Liya'})
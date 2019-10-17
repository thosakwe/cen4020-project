from django.shortcuts import render
from .models import Review
from game.models import Games

# Create your views here.
def home(request):
    lst =[1,2,3,4]
    context = {'games': Games.objects.all(),'list':lst}
    return render(request, 'review/home.html', context)

def about(request):
    return render(request, 'review/about.html', {'title':'About'})
# def home(request):
#     context = {
#         'reviews': Review.objects.all()
#     }
#     return render(request, 'review/home.html', context)

# def about(request):
#     return render(request, 'review/about.html', {'title':'About'})
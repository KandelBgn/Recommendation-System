from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')


def displayMovie(request):
    return render(request, 'displayMovie.html')

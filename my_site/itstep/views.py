from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def index(request):
    return render(request, "itstep/index.html")

def exercises(request):
    return HttpResponse(f'Articles by exercises')

def archive(request, cat):
    return HttpResponse(f'Archive by {cat}')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found :(</h1>')

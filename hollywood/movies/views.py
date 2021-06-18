from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie, Genre
from datetime import date
from .forms import *

from actors.models import Actor
from django.views.generic import CreateView
from django.utils import timezone
# Create your views here.


def movie_new(request):
    if request.method == "POST":
        form = AddMovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.created_at = timezone.now()
            movie.save()
            return redirect(f"/movies/{movie.pk}")
            # HttpResponse("<h3>Movie was saved</h3>")
        print(form.errors)
        return HttpResponse("<h3>Error</h3>")
    else:
        form = AddMovieForm()
        context = {'form': form}
        return render(request, 'movies/create_movie_form.html', context)



def movies(request):
    context = {'movies': Movie.objects.all()}
    return render(request, 'movies/movies.html', context)

def index(request):
    return render(request, 'movies/index.html')



def movies_numb(request, numb):
    context = {'move': Movie.objects.get(pk=numb)}
    return render(request, 'movies/moves_numb.html', context)


def add_actor(request):
    if request.method == "POST":
        form = AddActorForm(request.POST)
        if form.is_valid():
            actor = form.save(commit=False)
            actor.save()
            return HttpResponse("<h3>Actor was saved</h3>")
        print(form.errors)
        return HttpResponse("<h3>Error</h3>")
    else:
        form = AddActorForm()
        context = {'form': form}
        return render(request, 'movies/create_actor_form.html', context)

def add_genre(request):
    if request.method == "POST":
        form = AddGenreForm(request.POST)
        if form.is_valid():
            genre = form.save(commit=False)
            genre.save()
            return HttpResponse("<h3>Genre was saved</h3>")
        print(form.errors)
        return HttpResponse("<h3>Error</h3>")
    else:
        form = AddGenreForm()
        context = {'form': form}
        return render(request, 'movies/create_genre_form.html', context)

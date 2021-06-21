from django.forms import models
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie, Genre
from datetime import date
from .forms import AddMovieForm, FeedbackForm

from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from actors.models import Actor
from django.utils import timezone
# Create your views here.

class MovieListView(ListView):
    model = Movie
    context_object_name = 'movies'

def movies_list(request):
    return render(request, 'movies/movies_list.html', {'movies': Movie.objects.all()})

def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            return HttpResponse("<p>Thx you for your feedback</p>")
        else:
            return HttpResponse(form.errors)
    else:
        return render(request, 'movies/feedback.html', {'form': FeedbackForm()})


def index(request):
    return render(request, 'movies/index.html')

@login_required
def movie_new(request):
    if request.method == "POST":
        form = AddMovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.created_at = timezone.now()
            movie.user = request.user
            movie.save()
            return HttpResponse("<h3>Movie was saved</h3>")
        print(form.errors)
        return HttpResponse("<h3>Error</h3>")
    else:
        form = AddMovieForm()
        movies = Movie.objects.all()
        context = {'form': form, 'objects': movies}
        return render(request, 'movies/create_movie_form.html', context)

@login_required
def movie_added_me(request):
    return render(request, 'movies/movies_list.html', {'movies': Movie.objects.all().filter(user=request.user)})
    # if request.method == "POST":
    #     form = AddMovieForm(request.POST)
    #     if form.is_valid():
    #         movie = form.save(commit=False)
    #         movie.created_at = timezone.now()
    #         movie.user = request.user
    #         movie.save()
    #         return HttpResponse("<h3>Movie was saved</h3>")
    #     print(form.errors)
    #     return HttpResponse("<h3>Error</h3>")
    # else:
    #     form = AddMovieForm()
    #     movies = Movie.objects.all()
    #     context = {'form': form, 'objects': movies}
    #     return render(request, 'movies/create_movie_form.html', context)

























def add_actor(request):
    mell = Actor.objects.get(first_name="Mell")
    mell.movies.all()
    new_movie = Movie(name="Lalaland", year=date(2019, 2, 4), genre=Genre.objects.get(pk=1))
    new_movie.save()
    new_movie.actors.add(mell)
    new_movie.save()
    return HttpResponse("Mell was added")
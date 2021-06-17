from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie, Genre
from datetime import date
from .forms import AddMovieForm

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



def movies_numb(request, numb):
    context = {'move': Movie.objects.get(pk=numb)}
    return render(request, 'movies/moves_numb.html', context)






















def add_actor(request):
    mell = Actor.objects.get(first_name="Mell")
    mell.movies.all()
    new_movie = Movie(name="Lalaland", year=date(2019, 2, 4), genre=Genre.objects.get(pk=1))
    new_movie.save()
    new_movie.actors.add(mell)
    new_movie.save()
    return HttpResponse("Mell was added")
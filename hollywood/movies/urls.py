from django.urls import path
from .views import *
from .forms import *

urlpatterns = [
    path("add-actor/", add_actor, name='add_actor'),
    path("add-genre/", add_genre, name='add_genre'),
    path("add-movie/", movie_new, name='add_movie'),
    path("movies/", movies, name='movies'),
    path("movies/<int:numb>/", movies_numb, name='movies_numb'),
    path("movies/<int:numb>/change/", movie_change, name='movie_change'),
    path("", index, name='home'),
]

from django.urls import path
from .views import *

urlpatterns = [
    path("add-mell/", add_actor),
    path("add-genre/", add_genre),
    path("add-movie/", movie_new),
    path("movies/", movies),
    path("movies/<int:numb>/", movies_numb),
    path("", index),
]

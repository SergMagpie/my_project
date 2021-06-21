from django.urls import path
from .views import add_actor, movie_new, feedback_view, index, MovieListView, movies_list, movie_added_me

urlpatterns = [
    path("", index),
    path("add-movie", movie_new, name="add-movie"),
    path("movie-list", movies_list, name="movie-list"),
    path("feedback", feedback_view),
    path("movie-added-me", movie_added_me, name="movie-added-me"),
]

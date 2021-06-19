from django import forms
from django.db.models import fields
from .models import Movie, Genre
from actors.models import Actor


class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        exclude = ["created_at", ]


class AddActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = "__all__"


class AddGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"

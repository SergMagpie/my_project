from django import forms
from django.db.models import fields
from .models import Movie

class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        exclude = ["created_at",]
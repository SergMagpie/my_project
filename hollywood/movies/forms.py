from django import forms
from django.db.models import fields
from .models import Movie

class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        exclude = ["created_at", "user"]


class FeedbackForm(forms.Form):
    text = forms.CharField(label="You feedback here:", help_text="HELP TEXT", max_length=30)
    name = forms.CharField(label="Your name", max_length=40)
    email = forms.EmailField(label="Enter your email")
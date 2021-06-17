from django.contrib import admin
from django.db.models import fields
from django.forms.models import ModelForm
from .models import Genre, Movie
from django import forms

# Register your models here.

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


class MovieAdminForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        exclude = ["year"]

    
    # def clean_name(self):
    #     if self.cleaned_data["name"] == self.cleaned_data["name"].upper():
    #         raise forms.ValidationError("Empty field")

    #     return self.cleaned_data["name"]
    

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "genre", "actors_count")
    list_filter = ("year",)

    search_fields = ("name",)
    
    form = MovieAdminForm

    def actors_count(self, obj):
        actors_count = obj.actors.all().count()
        return actors_count

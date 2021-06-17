from django.db import models
from django.db.models.fields import CharField
from actors.models import Actor


class Genre(models.Model):
    """
    Action
    ScienceFiction
    Horror
    Musical
    """
    name = CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.DateField(blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor, related_name="movies")
    created_at = models.DateTimeField(blank=False, null=False)
    "Blade Runner -> ScienceFiction"

    def __str__(self) -> str:
        return f"{self.name} - {self.year}"
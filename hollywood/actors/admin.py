from django.contrib import admin
from django.db import models
from .models import Actor
# Register your models here.


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass
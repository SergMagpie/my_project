from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('exercises/', exercises, name='cats'),
    path('exercises/<slug:cat>', archive),
]
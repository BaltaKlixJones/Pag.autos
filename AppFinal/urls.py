from django.urls import path
from .views import *


urlpatterns = [
    path("", inicio, name= "inicio"),
    path("volkswagen/", vksw, name= "vw"),
    path("bmw/", bmws, name= "bmw"),
    path("mercedes/", merc, name= "mercedes"),
    path("ferrari/", ferrari, name= "ferrari"),
    path("audi/", audi, name= "audi"),
    path("lamborgini/", lamborgini, name= "lamborgini"),
    path('landing/', land, name='landing'),
    path('elements/', elem, name='elements'),
    path('generic/', gen, name='generic'),
    path('registrarse/', registrarse, name='registrarse'),
]
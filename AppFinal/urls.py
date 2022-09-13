from django.urls import path
from .views import *



urlpatterns = [
    path("", inicio, name= "inicio"),
    path("volkswagen/", auto_vksw, name= "vw"),
    path("bmw/", auto_bmw, name= "bmw"),
    path("mercedes/", auto_mercedes, name= "mercedes"),
    path("ferrari/", auto_ferrari, name= "ferrari"),
    path("auto_audi/", auto_audi, name= "audi"),
    path("lamborgini/", auto_lamborgini, name= "lamborgini"),
    path('landing/', land, name='landing'),
    path('elements/', elem, name='elements'),
    path('generic/', gen, name='generic'),
    path('registrarse/', registrarse, name='registrarse'),
]
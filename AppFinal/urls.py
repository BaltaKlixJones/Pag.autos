from django.urls import path
from .views import *



urlpatterns = [
    path("", inicio, name= "inicio"),
    path("autos/", autos, name= "autos"),
    path("motos/", motos, name= "motos"),
    path("aviones/", aviones, name= "aviones"),
    path("camiones/", camiones, name= "camiones"),
    path("autosform/", autosform, name= "autosform"),
    path('landing/', land, name='landing'),
    path('elements/', elem, name='elements'),
    path('generic/', gen, name='generic'),
    path('registrarse/', registrarse, name='registrarse'),
]
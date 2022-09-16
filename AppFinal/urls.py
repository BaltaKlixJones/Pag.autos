from django.urls import path
from .views import *



urlpatterns = [
    path("", inicio, name= "inicio"),
    path("motos/", motos, name= "motos"),
    path("aviones/", aviones, name= "aviones"),
    path("camiones/", camiones, name= "camiones"),
    path("autos/", autosform, name= "autos"),
    path('landing/', land, name='landing'),
    path('elements/', elem, name='elements'),
    path('generic/', gen, name='generic'),
    path('registrarse/', registrarse, name='registrarse'),
]
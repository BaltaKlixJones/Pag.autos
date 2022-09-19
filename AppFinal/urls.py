from django.urls import path
from .views import *



urlpatterns = [
    path("", inicio, name= "inicio"),
    path("motos/", motos, name= "motos"),
    path("aviones/", aviones, name= "aviones"),
    path("camiones/", camiones, name= "camiones"),
    path("autos/", autos, name= "autos"),
    path("buscar/", buscar, name="buscar"),
    path('registrarse/', registrarse, name='registrarse'),
    path('elements/', elem, name='elements')
]
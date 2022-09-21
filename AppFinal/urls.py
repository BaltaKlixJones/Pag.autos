from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", inicio, name= "inicio"),
    path("motos/", motos, name= "motos"),
    path("aviones/", aviones, name= "aviones"),
    path("camiones/", camiones, name= "camiones"),
    path("autos/", autos, name= "autos"),
    path("buscar/", buscar, name="buscar"),
    # Autos
    path("leerautos/", leerautos, name="leerautos"),
    path("eliminarAuto/<id>", eliminarAuto, name="eliminarAuto"),
    path("editarAuto/<id>", editarAutos, name="editarAuto"),
    # Motos
    path("leermotos/", leermotos, name="leermotos"),
    path("eliminarMoto/<id>", eliminarMoto, name="eliminarMoto"),
    path("editarMoto/<id>", editarMotos, name="editarMoto"),
    # Camiones
    path("leercamiones/", leercamiones, name="leercamiones"),
    path("eliminarCamion/<id>", eliminarCamion, name="eliminarCamion"),
    path("editarCamion/<id>", editarCamiones, name="editarCamion"),

    # Otro
    path("login/", login_request, name='login'),
    path('register/', register, name= 'register'),
    path('logout/', LogoutView.as_view (template_name= "AppFinal/logout.html"), name= 'logout'),
    path('elements/', elem, name='elements'),
]
from django.shortcuts import render
from django.http import HttpResponse
from .models import Autos, Motos, Aviones, Camiones

# Create your views here.


def inicio(request):
    return render (request, "AppFinal/inicio.html")


def motos(request):
    return render (request, "AppFinal/motos.html")

def camiones(request):
    return render (request, "AppFinal/camiones.html")

def aviones(request):
    return render (request, "AppFinal/aviones.html")


def land(request):
    return render (request, "AppFinal/landing.html")

def gen(request):
    return render (request, "AppFinal/generic.html")

def elem(request):
    return render (request, "AppFinal/elements.html")

def registrarse(request):
    return render (request, "AppFinal/registrarse.html") 

def autos(request):
    if request.method == "POST":
        marca=request.POST.get("marca")
        modelo=request.POST.get("modelo")
        color=request.POST.get("color")
        anio=request.POST.get("anio")
        auto= Autos(marca= marca, modelo= modelo, color= color, anio= anio)
        auto.save()
        return render( request, "AppFinal/padre.html")
    return render (request, "AppFinal/autos.html")





def nosotros(request):
    pass


# Creando paginas 

def inicio(request):
    return render (request, "AppFinal/inicio.html")

def land(request):
    return render (request, "AppFinal/landing.html")

def gen(request):
    return render (request, "AppFinal/generic.html")

def elem(request):
    return render (request, "AppFinal/elements.html")

def registrarse(request):
    return render (request, "AppFinal/registrarse.html") 
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def inicio(request):
    return render (request, "AppFinal/inicio.html")

def autos(request):
    return render (request, "AppFinal/autos.html")

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

def autosform(request):
    if request.method== "POST":
        marca=request.POST.get("marca")
        color=request.POST.get("color")
        auto_nuevo= Autos(marca=marca, color= color)
        auto_nuevo.save()
        return render( request, "AppFinal/inicio.html")
    return render( request, "AppFinal/autosform.html")





def nosotros(request):
    pass










"""
def volkswagen(request):
    volkswagen = Vw(modelo ="Vento", color="Gris", fabricacion="Alemania", anio_fabricacion= 1934 )
    volkswagen.save()
    texto = f"Auto creado: {volkswagen.modelo}, {volkswagen.nombre} ,{volkswagen.fabricacion}.Fecha de fabricacion de la marca: {volkswagen.anio_fabricacion}"
    return HttpResponse(texto)

def bmw(request):
    bmw = Bmw(modelo ="Z4", color="Negro", fabricacion="Alemania", anio_fabricacion= 1916)
    bmw.save()
    texto = f"Auto creado: {bmw.modelo}, {bmw.nombre} ,{bmw.fabricacion}.Fecha de fabricacion de la marca:{bmw.anio_fabricacion} "
    return HttpResponse(texto)

def ferrari(request):
    ferrari = Ferrari(modelo ="f40", color="Rojo", fabricacion="Italia", anio_fabricacion=1987)
    ferrari.save()
    texto = f"Auto creado:{ferrari.modelo}, {ferrari.nombre} ,{ferrari.fabricacion}.Fecha de fabricacion de la marca: {ferrari.anio_fabricacion} "
    return HttpResponse(texto)

def audi1(request):
    audi = Audi(modelo ="TT", color="azul", fabricacion="Alemaia", anio_fabricacion=1926)
    audi.save()
    texto = f"Auto creado:{audi.modelo}, {audi.nombre} ,{auto_audi.fabricacion}.Fecha de fabricacion de la marca: {audi.anio_fabricacion} "
    return HttpResponse(texto)

def lambo(request):
    lambo = Lambo(modelo ="Gallardo", color="amarillo", fabricacion="Italia", anio_fabricacion=2020)
    lambo.save()
    texto = f"Auto creado:{lambo.modelo}, {lambo.nombre} ,{lambo.fabricacion}.Fecha de fabricacion de la marca: {lambo.anio_fabricacion} "
    return HttpResponse(texto)

def mercedes(request):
    mercedes = Mercedes(modelo ="GLC", color="Blanco", fabricacion="Alemaia", anio_fabricacion=1926)
    mercedes.save()
    texto = f"Auto creado:{mercedes.modelo}, {mercedes.nombre} ,{mercedes.fabricacion}.Fecha de fabricacion de la marca: {mercedes.anio_fabricacion} "
    return HttpResponse(texto)
    """


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
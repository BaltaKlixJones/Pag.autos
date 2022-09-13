from re import X
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

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
    ferrari = Ferrari(modelo ="GLC", color="Rojo", fabricacion="Italia", anio_fabricacion=1926)
    ferrari.save()
    texto = f"Auto creado:{ferrari.modelo}, {ferrari.nombre} ,{ferrari.fabricacion}.Fecha de fabricacion de la marca: {ferrari.anio_fabricacion} "
    return HttpResponse(texto)

def audi(request):
    audi = Audi(modelo ="TT", color="azul", fabricacion="Alemaia", anio_fabricacion=1926)
    audi.save()
    texto = f"Auto creado:{audi.modelo}, {audi.nombre} ,{audi.fabricacion}.Fecha de fabricacion de la marca: {audi.anio_fabricacion} "
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


# Creando paginas 
def inicio(request):
    return render (request, "AppFinal/inicio.html")

def vksw(request):
    return render (request, "AppFinal/vw.html")

def bmws(request):
    return render (request, "AppFinal/bmw.html")

def merc(request):
    return render (request, "AppFinal/mercedes.html")

def audi_audi(request):
    return render (request, "AppFinal/audi.html")

def lamborgini(request):
    return render (request, "AppFinal/lamborgini.html")

def ferr(request):
    return render (request, "AppFinal/ferrari.html")
    
def land(request):
    return render (request, "AppFinal/landing.html")

def gen(request):
    return render (request, "AppFinal/generic.html")

def elem(request):
    return render (request, "AppFinal/elements.html")

def registrarse(request):
    return render (request, "AppFinal/registrarse.html")
from re import X
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def auto_volkswagen(request):
    auto_volkswagen = Vw(modelo ="Vento", color="Gris", fabricacion="Alemania", anio_fabricacion= 1934 )
    auto_volkswagen.save()
    texto = f"Auto creado: {auto_volkswagen.modelo}, {auto_volkswagen.nombre} ,{auto_volkswagen.fabricacion}.Fecha de fabricacion de la marca: {auto_volkswagen.anio_fabricacion}"
    return HttpResponse(texto)

def auto_bmw(request):
    auto_bmw = Bmw(modelo ="Z4", color="Negro", fabricacion="Alemania", anio_fabricacion= 1916)
    auto_bmw.save()
    texto = f"Auto creado: {auto_bmw.modelo}, {auto_bmw.nombre} ,{auto_bmw.fabricacion}.Fecha de fabricacion de la marca:{auto_bmw.anio_fabricacion} "
    return HttpResponse(texto)

def auto_ferrari(request):
    auto_ferrari = Ferrari(modelo ="f40", color="Rojo", fabricacion="Italia", anio_fabricacion=1987)
    auto_ferrari.save()
    texto = f"Auto creado:{auto_ferrari.modelo}, {auto_ferrari.nombre} ,{auto_ferrari.fabricacion}.Fecha de fabricacion de la marca: {auto_ferrari.anio_fabricacion} "
    return HttpResponse(texto)

def auto_audi(request):
    auto_audi = Audi(modelo ="TT", color="azul", fabricacion="Alemaia", anio_fabricacion=1926)
    auto_audi.save()
    texto = f"Auto creado:{auto_audi.modelo}, {auto_audi.nombre} ,{auto_audi.fabricacion}.Fecha de fabricacion de la marca: {auto_audi.anio_fabricacion} "
    return HttpResponse(texto)

def auto_lambo(request):
    auto_lambo = Lambo(modelo ="Gallardo", color="amarillo", fabricacion="Italia", anio_fabricacion=2020)
    auto_lambo.save()
    texto = f"Auto creado:{auto_lambo.modelo}, {auto_lambo.nombre} ,{auto_lambo.fabricacion}.Fecha de fabricacion de la marca: {auto_lambo.anio_fabricacion} "
    return HttpResponse(texto)

def auto_mercedes(request):
    auto_mercedes = Mercedes(modelo ="GLC", color="Blanco", fabricacion="Alemaia", anio_fabricacion=1926)
    auto_mercedes.save()
    texto = f"Auto creado:{auto_mercedes.modelo}, {auto_mercedes.nombre} ,{auto_mercedes.fabricacion}.Fecha de fabricacion de la marca: {auto_mercedes.anio_fabricacion} "
    return HttpResponse(texto)


# Creando paginas 
def inicio(request):
    return render (request, "AppFinal/inicio.html")

def vksw(request):
    return render (request, "AppFinal/vw.html")

def bmw(request):
    return render (request, "AppFinal/bmw.html")

def mercedes(request):
    return render (request, "AppFinal/mercedes.html")

def audi(request):
    return render (request, "AppFinal/audi.html")

def lamborgini(request):
    return render (request, "AppFinal/lamborgini.html")

def ferrari(request):
    return render (request, "AppFinal/ferrari.html")
    
def land(request):
    return render (request, "AppFinal/landing.html")

def gen(request):
    return render (request, "AppFinal/generic.html")

def elem(request):
    return render (request, "AppFinal/elements.html")

def registrarse(request):
    return render (request, "AppFinal/registrarse.html")
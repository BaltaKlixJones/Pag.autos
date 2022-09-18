from django.shortcuts import render
from django.http import HttpResponse
from .forms import AutoFormulario, MotoFormulario, AvionFormulario, CamionFormulario
from .models import Autos, Motos, Aviones, Camiones

# Create your views here.


def inicio(request):
    return render (request, "AppFinal/inicio.html")

def autos(request):
    if request.method == "POST":
        miFormulario= AutoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            marca= info.get("marca")
            modelo= info.get("modelo")
            color= info.get("color")
            año= info.get("año")
            auto= Autos(marca= marca, modelo= modelo, color= color, año= año)
            auto.save()
            return render (request, "AppFinal/autos.html", {"mensaje": "Auto creado con exito!"})
        else:
            return render(request, "AppFinal/autos.html", {"mensaje": "Error!"} )
    else:
        miFormulario= AutoFormulario()
        return render (request, "AppFinal/autos.html", {"formulario": miFormulario})



def motos(request):
    if request.method == "POST":
        miFormulario= MotoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            marca= info.get("marca")
            modelo= info.get("modelo")
            color= info.get("color")
            año= info.get("año")
            moto= Motos(marca= marca, modelo= modelo, color= color, año= año)
            moto.save()
            return render (request, "AppFinal/motos.html", {"mensaje": "Moto creada con exito!"})
        else:
            return render(request, "AppFinal/motos.html", {"mensaje": "Error!"} )
    else:
        miFormulario= MotoFormulario()
        return render (request, "AppFinal/motos.html", {"formulario": miFormulario})



def camiones(request):
    if request.method == "POST":
        miFormulario= CamionFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            marca= info.get("marca")
            modelo= info.get("modelo")
            color= info.get("color")
            año= info.get("año")
            camion= Camiones(marca= marca, modelo= modelo, color= color, año= año)
            camion.save()
            return render (request, "AppFinal/camiones.html", {"mensaje": "Camion creado con exito!"})
        else:
            return render(request, "AppFinal/camiones.html", {"mensaje": "Error!"} )
    else:
        miFormulario= CamionFormulario()
        return render (request, "AppFinal/camiones.html", {"formulario": miFormulario})


def aviones(request):
    if request.method == "POST":
        miFormulario= AvionFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            modelo= info.get("modelo")
            color= info.get("color")
            año= info.get("año")
            avion= Aviones( modelo= modelo, color= color, año= año)
            avion.save()
            return render (request, "AppFinal/aviones.html", {"mensaje": "Avion creado con exito!"})
        else:
            return render(request, "AppFinal/aviones.html", {"mensaje": "Error!"} )
    else:
        miFormulario= AvionFormulario()
        return render (request, "AppFinal/aviones.html", {"formulario": miFormulario})



def buscarAuto(request):
    return render (request, "AppFinal/buscarAuto.html")


def buscar(request):
    if request.GET["marca"]:
        marca= request.GET["marca"]
        autos_marca= Autos.objects.filter(marca__icontains= marca)
        if len(autos_marca) !=0:
            return render(request, "AppFinal/resultadoBusqueda.html", {"autos": autos_marca})
        else:
            return render(request, "AppFinal/resultadoBusqueda.html", {"mensaje": "No se encontraron resultados"})
    else:
        return render (request, "AppFinal/buscarAuto.html", {"mensaje": "No se enviaron datos"})
    







def nosotros(request):
    pass


# Creando paginas 

def land(request):
    return render (request, "AppFinal/landing.html")

def gen(request):
    return render (request, "AppFinal/generic.html")

def elem(request):
    return render (request, "AppFinal/elements.html")

def registrarse(request):
    return render (request, "AppFinal/registrarse.html") 

    # FORMULARIO A MANO

"""
def autos(request):

    if request.method == "POST":
        marca=request.POST.get("marca")
        modelo=request.POST.get("modelo")
        color=request.POST.get("color")
        anio=request.POST.get("anio")
        auto= Autos(marca= marca, modelo= modelo, color= color, anio= anio)
        auto.save()
        return render (request, "AppFinal/inicio.html")

    return render (request, "AppFinal/autos.html")
    """
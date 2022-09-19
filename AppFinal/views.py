from django.shortcuts import render
from django.http import HttpResponse
from .forms import AutoFormulario, MotoFormulario, AvionFormulario, CamionFormulario
from .models import Autos, Motos, Aviones, Camiones

# Create your views here.


def inicio(request):
    return render (request, "AppFinal/inicio.html")

#.............................................................................#

# SECCION AUTOS 
# Pagina para crear y ver autos

def autos(request):
    ver_autos= Autos.objects.all()
    if request.method == "POST":
        miFormulario= AutoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            auto=Autos(marca= info['marca'], modelo= info['modelo'], color=info['color'], año= info['año'])
            auto.save()
            return render (request, "AppFinal/autos.html", {"mensaje": "Auto creado con exito!" , "ver_autos": ver_autos})
        else:
            return render(request, "AppFinal/autos.html", {"mensaje": "Error!"} )
    else:
        miFormulario= AutoFormulario()

    return render (request, "AppFinal/autos.html", {"formulario": miFormulario,  "ver_autos": ver_autos})


# ver autos para editar

def leerautos(request):
    leerautos= Autos.objects.all()
    return render (request, "AppFinal/leerautos.html", {"leerautos": leerautos})


# eliminar autos

def eliminarAuto(request, id ):
    eliminar_auto= Autos.objects.get(id=id)
    eliminar_auto.delete()
    leerautos= Autos.objects.all()
    return render (request, "AppFinal/leerautos.html", {"leerautos": leerautos, "mensaje": "Auto eliminado!"})


# editar autos

def editarAutos(request, id):
    auto = Autos.objects.get(id=id)
    if request.method == "POST":
        form = AutoFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            auto.marca = info["marca"]
            auto.modelo = info["modelo"]
            auto.color = info["color"]
            auto.año = info["año"]
            auto.save()
            leerautos= Autos.objects.all()
            return render (request, "AppFinal/leerautos.html", {"leerautos": leerautos, "mensaje": "Auto editado!"})

    else:
        formulario = AutoFormulario(initial={"marca": auto.marca , "modelo": auto.modelo , "color": auto.color , "año": auto.año})
        return render (request, "AppFinal/editarAutos.html", {"formulario": formulario, "auto_marca": auto.marca , "id":auto.id})





#.............................................................................#

# SECCION MOTOS 
# Pagina para crear y ver motos

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




#.............................................................................#

# SECCION CAMIONES
# Pagina para crear y ver camiones

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



#.............................................................................#

# SECCION AVIONES
# Pagina para crear y ver aviones

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
        return render (request, "AppFinal/autos.html", {"mensaje": "No se enviaron datos!"})
    

def buscar(request):
    if request.GET["marca"]:
        marca= request.GET["marca"]
        autos_marca= Autos.objects.filter(marca__icontains= marca)
        if len(autos_marca) !=0:
            return render(request, "AppFinal/resultadoBusqueda.html", {"autos": autos_marca})
        else:
            return render(request, "AppFinal/resultadoBusqueda.html", {"mensaje": "No se encontraron resultados"})
    else:
        return render (request, "AppFinal/resultadoBusqueda.html", {"mensaje": "No se enviaron datos!"})




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


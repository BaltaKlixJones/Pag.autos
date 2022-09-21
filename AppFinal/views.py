from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import AutoFormulario, MotoFormulario, AvionFormulario, CamionFormulario, UserRegisterForm
from .models import Autos, Motos, Aviones, Camiones

# Create your views here.


def inicio(request):
    return render (request, "AppFinal/inicio.html")

#.............................................................................#
# login
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu= request.POST["username"]
            clave= request.POST["password"]

            usuario = authenticate(username= usu, password= clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppFinal/inicio.html", {'form':form, 'mensaje': f"Bienvenido {usuario}"})
            else:
                return render (request, "AppFinal/login.html", {'form':form, 'mensaje': 'Usuario o contraseña incorrectos'})
        else:
            return render (request, "AppFinal/login.html", {'form':form, 'mensaje': 'Usuario o contraseña incorrectos'})
    else:
        form = AuthenticationForm()
        return render (request, "AppFinal/login.html", {'form': form})


# registro

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render (request, "AppFinal/inicio.html", {'mensaje': f"Usuario creado! \n Bienvenido {username}!"})
    else:
        form = UserRegisterForm()
    return render (request, "AppFinal/register.html", {'form': form})

# logout




#.............................................................................#

# SECCION AUTOS 
# Pagina para crear y ver autos

@login_required
def autos(request):
    ver_autos= Autos.objects.all()
    if request.method == "POST":
        miFormulario= AutoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            auto=Autos(marca= info['marca'], modelo= info['modelo'], color=info['color'], año= info['año'])
            auto.save()
            return render (request, "AppFinal/autos.html", {"formulario": miFormulario, "mensaje": "Auto creado con exito!" , "ver_autos": ver_autos})
        else:
            return render(request, "AppFinal/autos.html", {"mensaje": "Error!"} )
    else:
        miFormulario= AutoFormulario()

    return render (request, "AppFinal/autos.html", {"formulario": miFormulario,  "ver_autos": ver_autos})

# buscar auto

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
@login_required
def motos(request):
    ver_motos= Motos.objects.all()
    if request.method == "POST":
        miFormulario= AutoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            motos=Motos(marca= info['marca'], modelo= info['modelo'], color=info['color'], año= info['año'])
            motos.save()
            return render (request, "AppFinal/motos.html", {"formulario": miFormulario, "mensaje": "Moto creado con exito!" , "ver_motos": ver_motos})
        else:
            return render(request, "AppFinal/motos.html", {"mensaje": "Error!"} )
    else:
        miFormulario = MotoFormulario()

    return render (request, "AppFinal/motos.html", {"formulario": miFormulario,  "ver_motos": ver_motos})

#buscar moto

def buscar(request):
    if request.GET["marca"]:
        marca= request.GET["marca"]
        motos_marca= Motos.objects.filter(marca__icontains= marca)
        if len(motos_marca) !=0:
            return render(request, "AppFinal/resultadoBusquedaMoto.html", {"motos": motos_marca})
        else:
            return render(request, "AppFinal/resultadoBusquedaMoto.html", {"mensaje": "No se encontraron resultados"})
    else:
        return render (request, "AppFinal/resultadoBusquedaMoto.html", {"mensaje": "No se enviaron datos!"})
# ver motos para editar

def leermotos(request):
    leermotos= Motos.objects.all()
    return render (request, "AppFinal/leermotos.html", {"leermotos": leermotos})

# elminar motos

def eliminarMoto(request, id ):
    eliminar_moto= Motos.objects.get(id=id)
    eliminar_moto.delete()
    leermotos= Motos.objects.all()
    return render (request, "AppFinal/leermotos.html", {"leermotos": leermotos, "mensaje": "Moto eliminada!"})
# editar motos


def editarMotos(request, id):
    moto = Motos.objects.get(id=id)
    if request.method == "POST":
        form = MotoFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            moto.marca = info["marca"]
            moto.modelo = info["modelo"]
            moto.color = info["color"]
            moto.año = info["año"]
            moto.save()
            leermotos= Motos.objects.all()
            return render (request, "AppFinal/leermotos.html", {"leermotos": leermotos, "mensaje": "Moto editada!"})

    else:
        formulario = MotoFormulario(initial={"marca": moto.marca , "modelo": moto.modelo , "color": moto.color , "año": moto.año})
        return render (request, "AppFinal/editarMotos.html", {"formulario": formulario, "motos_marca": moto.marca , "id":moto.id})

#.............................................................................#

# SECCION CAMIONES
# Pagina para crear y ver camiones
@login_required
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

# buscar camion

# ver camiones para editar

# elminar camiones

# editar camiones

#.............................................................................#

# SECCION AVIONES
# Pagina para crear y ver aviones
@login_required
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

# Buscar avion 


# ver aviones para editar

# elminar aviones

# editar aviones



def nosotros(request):
    pass


# Creando paginas 






def land(request):
    return render (request, "AppFinal/landing.html")

def gen(request):
    return render (request, "AppFinal/generic.html")

def elem(request):
    return render (request, "AppFinal/elements.html")




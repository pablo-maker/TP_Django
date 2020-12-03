from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("usuarios:login"))
    return render(request, "usuarios/usuario.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None: #si existe el usuario
            login(request, user)
            #ver a que grupo pertenece
            if user.groups.filter(name='Secretarios').exists() :
                return HttpResponseRedirect(reverse("turnos:index"))
            elif user.groups.filter(name='Medicos').exists() :
                return HttpResponseRedirect(reverse("medicos:index"))
            elif user.groups.filter(name='Ventas').exists() :
                return HttpResponseRedirect(reverse("ventas:index"))
            elif user.groups.filter(name='Talleres').exists() :
                return HttpResponseRedirect(reverse("talleres:index"))
            elif user.groups.filter(name='Gerentes').exists() :
                return HttpResponseRedirect(reverse("gerencias:index"))
            else:
                return HttpResponseRedirect(reverse("usuarios:index"))
        else:
            return render(request, "usuarios/login.html", {
                "mensaje": "Credenciales no validas."
            })
    else:
        return render(request, "usuarios/login.html")

def logout_view(request):
    logout(request)
    return render(request, "usuarios/login.html", {
        "mensaje": "Desconectado."
    })

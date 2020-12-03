from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.urls import reverse     
from django.contrib.auth.models import User
from ventas.models import Pedidos
# Create your views here.
def index(request):
    return render(request,"talleres/index.html",{
        "pedidos":Pedidos.objects.all(),
    })

def finalizado(request,pedido_id):
    try:
        pedido = Pedidos.objects.get(pk=int(pedido_id))
    except KeyError:
        return HttpResponseBadRequest("Bad Request: Elija una opcion")
    except Pedidos.DoesNotExist:
        return HttpResponseBadRequest("Bad Request: el Pedido no existe")
    pedido.estado = "Finalizado"
    pedido.save()
    return HttpResponseRedirect(reverse("talleres:index",))
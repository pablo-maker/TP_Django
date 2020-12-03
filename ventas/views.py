from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.urls import reverse     
from django.db.models import Sum
from django.contrib.auth.models import User
from .models import Pedidos,Productos
from turnos.models import Pacientes
import datetime
# Create your views here.
def index(request):
    return render(request,"ventas/index.html",{
        "pedidos":Pedidos.objects.all(),
        "pacientes":Pacientes.objects.all(),
        "productos":Productos.objects.all(),
    })

def nuevo_pedido(request):
    if request.method == "POST":
        try:
            paciente = Pacientes.objects.get(pk=int(request.POST["paciente"]))
            productos = Productos.objects.filter(pk__in=(request.POST.getlist("producto")))
            tipo_pago = request.POST["tipo_pago"]
        except KeyError:
            return HttpResponseBadRequest("Bad Request: Elija una opcion")
        except Productos.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: el producto no existe")
        except Pacientes.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: el paciente no existe")
        
        subtotal=productos.aggregate(Sum('precio'))
        subtotal = subtotal["precio__sum"]

        vendedor = request.user
        fecha = datetime.datetime.now().strftime('%Y-%m-%d')

        pedido = Pedidos(paciente=paciente,tipo_pago=tipo_pago,estado="Pendiente",subtotal=subtotal,vendedor=vendedor,fecha=fecha)
        pedido.save()
        pedido.producto.set(productos)
        return HttpResponseRedirect(reverse("ventas:index",))

def estado_pedido(request,pedido_id):
    try:
        pedido = Pedidos.objects.get(pk=int(pedido_id))
    except KeyError:
        return HttpResponseBadRequest("Bad Request: Elija una opcion")
    except Pedidos.DoesNotExist:
        return HttpResponseBadRequest("Bad Request: el Pedido no existe")
    pedido.estado = "Pedido"
    pedido.save()
    return HttpResponseRedirect(reverse("ventas:index",))

def estado_taller(request,pedido_id):
    try:
        pedido = Pedidos.objects.get(pk=int(pedido_id))
    except KeyError:
        return HttpResponseBadRequest("Bad Request: Elija una opcion")
    except Pedidos.DoesNotExist:
        return HttpResponseBadRequest("Bad Request: el Pedido no existe")
    pedido.estado = "Taller"
    pedido.save()
    return HttpResponseRedirect(reverse("ventas:index",))
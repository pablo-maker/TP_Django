from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.urls import reverse     
from django.contrib.auth.models import User
from django.db.models import Count
from turnos.models import Turnos
from ventas.models import Pedidos,Productos
from datetime import datetime, timedelta, date
import calendar
# Create your views here.
def index(request):
    return render(request,"gerencias/index.html",{
    })

def asistencias(request,rango):
    
    if rango=="semana":
        #primer y ultimo dia de la semana actual
        date_str = datetime.now().strftime('%Y-%m-%d')
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')

        start = date_obj - timedelta(days=date_obj.weekday())  # Monday
        end = start + timedelta(days=6)  # Sunday

        turnos = Turnos.objects.filter(fecha__range=[start,end],asistencia=True)
        return render(request,"gerencias/asistencias.html",{
            "turnos":turnos
        })
    elif rango=="mes":
        fecha_actual = datetime.now()
        start = date(fecha_actual.year,fecha_actual.month,1)
        end = date(fecha_actual.year,fecha_actual.month,calendar.monthrange(fecha_actual.year, fecha_actual.month)[1])

        turnos = Turnos.objects.filter(fecha__range=[start,end],asistencia=True)
        return render(request,"gerencias/asistencias.html",{
            "turnos":turnos
        })
    

def inasistencias(request,rango):
    if rango=="semana":
        #primer y ultimo dia de la semana actual
        date_str = datetime.now().strftime('%Y-%m-%d')
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')

        start = date_obj - timedelta(days=date_obj.weekday())  # Monday
        end = start + timedelta(days=6)  # Sunday

        turnos = Turnos.objects.filter(fecha__range=[start,end]).exclude(asistencia=True)
        return render(request,"gerencias/inasistencias.html",{
            "turnos":turnos
        })
    elif rango=="mes":
        fecha_actual = datetime.now()
        start = date(fecha_actual.year,fecha_actual.month,1)
        end = date(fecha_actual.year,fecha_actual.month,calendar.monthrange(fecha_actual.year, fecha_actual.month)[1])

        turnos = Turnos.objects.filter(fecha__range=[start,end]).exclude(asistencia=True)
        return render(request,"gerencias/inasistencias.html",{
            "turnos":turnos
        })


def pedidos(request,rango):
    if rango=="semana":
        #primer y ultimo dia de la semana actual
        date_str = datetime.now().strftime('%Y-%m-%d')
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')

        start = date_obj - timedelta(days=date_obj.weekday())  # Monday
        end = start + timedelta(days=6)  # Sunday

        pedido = Pedidos.objects.filter(fecha__range=[start,end])
        return render(request,"gerencias/pedidos.html",{
            "pedidos":pedido
        })
    elif rango=="mes":
        fecha_actual = datetime.now()
        start = date(fecha_actual.year,fecha_actual.month,1)
        end = date(fecha_actual.year,fecha_actual.month,calendar.monthrange(fecha_actual.year, fecha_actual.month)[1])

        pedido = Pedidos.objects.filter(fecha__range=[start,end])
        return render(request,"gerencias/pedidos.html",{
            "pedidos":pedido
        })

def productos(request):
    fecha_actual = datetime.now()
    start = date(fecha_actual.year,fecha_actual.month,1)
    end = date(fecha_actual.year,fecha_actual.month,calendar.monthrange(fecha_actual.year, fecha_actual.month)[1])

    productos = Pedidos.objects.filter(fecha__range=[start,end]).values('producto__nombre').annotate(Count('producto')).order_by('-producto__count')
    
    return render(request,"gerencias/productos.html",{
        "productos":productos
    })

def ventas(request):
    pedidos = Pedidos.objects.filter(fecha__year='2020').extra({'mes' : "MONTH(fecha)"}).values('vendedor__first_name','vendedor__last_name','fecha').annotate(total_item=Count('vendedor'))
   
    return render(request,"gerencias/ventas.html",{
        "pedidos":pedidos,
        "vendedor":Pedidos.objects.all()
    })
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.urls import reverse     
from django.contrib.auth.models import User
from .models import HistorialesMedico
from turnos.models import Turnos,Pacientes
# Create your views here.
def index(request):
    try:    
        pacientes = Turnos.objects.filter(medico=request.user.pk)
    except Turnos.DoesNotExist:
        raise Http404("No existen pacientes")
    return render(request,"medicos/index.html",{
        "pacientes":pacientes,
    })

def paciente(request,id_paciente):
    historial = HistorialesMedico.objects.filter(paciente=id_paciente)
    paciente = Pacientes.objects.get(id=id_paciente)
    return render(request,"medicos/paciente.html",{
        "historial":historial,
        "paciente":paciente
    })

def nuevo_detalle(request,id_paciente):
    if request.method == "POST":
        try:
            paciente = Pacientes.objects.get(pk=id_paciente)
        except KeyError:
            return HttpResponseBadRequest("Bad Request: complete la observacion")
        except Pacientes.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: el paciente no existe")
        historia = HistorialesMedico(paciente=paciente,detalle=request.POST["detalle"])
        historia.save()
        return HttpResponseRedirect(reverse("medicos:paciente", args=(id_paciente,)))

def filtrar(request):
    if request.method == "POST":
        try:
            fecha_desde = request.POST["fecha_desde"]
            fecha_hasta = request.POST["fecha_hasta"]
            paciente = Turnos.objects.filter(medico=request.user.pk,fecha__range=(fecha_desde,fecha_hasta))
        except KeyError:
            raise Http404("No existen pacientes para el rango de fecha indicado")
    return render(request,"medicos/index.html",{
        "pacientes":paciente,
        "fecha_filtro":str(fecha_desde)+" hasta la fecha "+str(fecha_hasta)
    })
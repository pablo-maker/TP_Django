from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.urls import reverse     
from django.contrib.auth.models import User
from .models import Pacientes,Turnos


# Create your views here.
def index(request):
    return render(request,"turnos/index.html", {
        "turnos":Turnos.objects.all(),
        "pacientes" : Pacientes.objects.all(),
        "medicos" : User.objects.filter(groups__name="Medicos")
    })

def turno(request,turno_id):
    try:
        turno = Turnos.objects.get(id=turno_id)
    except Turnos.DoesNotExist:
        raise Http404("Turno not found")
    return render(request,"turnos/turno.html",{
        "turno": turno,
        "pacientes" : Pacientes.objects.all(),
        "medicos" : User.objects.filter(groups__name="Medicos")
    })

def nuevo_turno(request):
    if request.method == "POST":
        try:
            paciente = Pacientes.objects.get(pk=int(request.POST["paciente"]))
            medico = User.objects.get(pk=int(request.POST["medico"]))
            fecha = request.POST["fecha"]
        except KeyError:
            return HttpResponseBadRequest("Bad Request: Elija una opcion")
        except User.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: el medico no existe")
        except Pacientes.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: el paciente no existe")
        turno = Turnos(paciente=paciente,medico=medico,fecha=fecha,asistencia=False)
        turno.save()
        return HttpResponseRedirect(reverse("turnos:turno", args=(turno.id,)))

def borrar(request,turno_id):
    try:
        turno = Turnos.objects.get(pk=turno_id)
    except KeyError:
        return HttpResponseBadRequest("Bad Request: Elija un turno")
    except Turnos.DoesNotExist:
        return HttpResponseBadRequest("Bad Request: El turno no existe")
    
    Turnos.objects.filter(pk=turno_id).delete()
    return HttpResponseRedirect(reverse("turnos:index",))

def editar(request,turno_id):
    if request.method == "POST":
        try:
            turno = Turnos.objects.get(pk=turno_id)
            paciente = Pacientes.objects.get(pk=int(request.POST["paciente"]))
            medico = User.objects.get(pk=int(request.POST["medico"]))
            fecha = request.POST["fecha"]
        except KeyError:
            return HttpResponseBadRequest("Bad Request: Elija un turno")
        except Turnos.DoesNotExist:            
            return HttpResponseBadRequest("Bad Request: El turno no existe")
        except User.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: el medico no existe")
        except Pacientes.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: el paciente no existe")
        turno.paciente = paciente
        turno.medico = medico
        turno.fecha = fecha
        turno.asistencia = request.POST["asistencia"]
        turno.save()
        return HttpResponseRedirect(reverse("turnos:turno", args=(turno.id,)))
        
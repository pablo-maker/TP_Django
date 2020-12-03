from django.urls import path

from . import views

app_name="medicos"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id_paciente>/paciente", views.paciente, name="paciente"),
    path("<int:id_paciente>/nuevo_detalle", views.nuevo_detalle, name="nuevo_detalle"),
    path("filtrar/", views.filtrar, name="filtrar"),
    
]
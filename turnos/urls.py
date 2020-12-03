from django.urls import path

from . import views

app_name="turnos"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:turno_id>", views.turno, name="turno"),
    path("nuevo_turno/", views.nuevo_turno, name="nuevo_turno"),
    path("<int:turno_id>/borrar", views.borrar, name="borrar"),
    path("<int:turno_id>/editar", views.editar, name="editar"),
]
from django.urls import path

from . import views

app_name="gerencias"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:rango>/asistencias", views.asistencias, name="asistencias"),
    path("<str:rango>/inasistencias", views.inasistencias, name="inasistencias"),
    path("<str:rango>/pedidos", views.pedidos, name="pedidos"),
    path("productos/", views.productos, name="productos"),
    path("ventas/", views.ventas, name="ventas"),
]
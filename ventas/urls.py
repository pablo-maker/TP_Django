from django.urls import path

from . import views

app_name="ventas"

urlpatterns = [
    path("", views.index, name="index"),
    path("nuevo_pedido/", views.nuevo_pedido, name="nuevo_pedido"),
    path("<int:pedido_id>/estado_pedido", views.estado_pedido, name="estado_pedido"),
    path("<int:pedido_id>/estado_taller", views.estado_taller, name="estado_taller"),

]
from django.urls import path

from . import views

app_name="talleres"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pedido_id>/finalizado", views.finalizado, name="finalizado"),
]
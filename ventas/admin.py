from django.contrib import admin

from .models import Productos,Pedidos
# Register your models here.

class PedidosAdmin(admin.ModelAdmin):
    filter_horizontal = ("__str__",)

class ProductosAdmin(admin.ModelAdmin):
    filter_horizontal = ("__str__",)

admin.site.register(Productos)
admin.site.register(Pedidos)
from django.contrib import admin

from .models import Pacientes,Turnos

# Register your models here.

class PacientesAdmin(admin.ModelAdmin):
    filter_horizontal = ("__str__","nombre",)

class TurnosAdmin(admin.ModelAdmin):
    filter_horizontal = ("__str__",)

admin.site.register(Pacientes)
admin.site.register(Turnos)
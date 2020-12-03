from django.contrib import admin
from .models import HistorialesMedico

# Register your models here.

class HistorialAdmin(admin.ModelAdmin):
    filter_horizontal = ("__str__")

admin.site.register(HistorialesMedico)
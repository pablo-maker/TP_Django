from django.db import models
from django.contrib.auth.models import User
from turnos.models import Pacientes
# Create your models here.

class HistorialesMedico(models.Model):
    paciente = models.ForeignKey(Pacientes,on_delete=models.CASCADE, related_name="historia_paciente")
    detalle = models.TextField()

    def __str__(self):
        return f"{self.paciente}: {self.detalle} "


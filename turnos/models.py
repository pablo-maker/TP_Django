from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pacientes(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nombre} {self.apellido} "


class Turnos(models.Model):
    paciente = models.ForeignKey(Pacientes,on_delete=models.CASCADE, related_name="turno_paciente")
    medico = models.ForeignKey(User,limit_choices_to={'groups__name':'Medicos'},on_delete=models.CASCADE, related_name="turno_medico")
    fecha = models.DateField()
    asistencia = models.BooleanField(blank=True,null=True)

    def __str__(self):
        return f"El paciente {self.paciente} tiene turno el dia {self.fecha} con el Medico: {self.medico}"

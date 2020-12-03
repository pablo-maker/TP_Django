from django.db import models
from django.contrib.auth.models import User
from turnos.models import Pacientes
# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=64)
    detalle = models.CharField(max_length=64)
    precio = models.IntegerField()
    tipo = models.CharField(max_length=15,blank=True,null=True)
    lado = models.CharField(max_length=15,blank=True,null=True)
    armazon = models.BooleanField(blank=True,null=True)

    def __str__(self):
        return f"{self.nombre} - {self.detalle}: {self.precio} "



class Pedidos(models.Model):
    paciente = models.ForeignKey(Pacientes,on_delete=models.CASCADE, related_name="pedido_paciente")
    producto = models.ManyToManyField(Productos,blank=True,related_name="pedidos_productos")
    subtotal = models.IntegerField()
    tipo_pago = models.CharField(max_length=64)
    estado = models.CharField(max_length=64)
    fecha = models.DateField()
    vendedor = models.ForeignKey(User,limit_choices_to={'groups__name':'Ventas'},on_delete=models.CASCADE, related_name="vendedor_pedido")
    def __str__(self):
        return f"Pedido Nº {self.id}: {self.paciente}, {self.subtotal}, {self.tipo_pago}, {self.estado}, {self.fecha}"


from django.db import models
from rest_framework import serializers
# Create your models here.


class Pais(models.Model):
  IdPais = models.IntegerField(primary_key=True)
  Nombre = models.CharField(max_length=40, null=False)

  def __str__(self):
    return f"{self.Nombre}"

class Empleado(models.Model):
  Nombre = models.CharField(max_length=50, null=False)
  FechaIngreso = models.DateTimeField(auto_now_add=True)
  LimiteCredito = models.DecimalField(max_digits=10, decimal_places=2, null=False)
  Pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.Nombre} {self.LimiteCredito} {self.FechaIngreso} {self.Pais}"
  

class EmpleadoSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  Nombre = serializers.CharField(max_length=50)
  FechaIngreso = serializers.DateTimeField()
  LimiteCredito = serializers.DecimalField(max_digits=10, decimal_places=2)
  Pais = serializers.PrimaryKeyRelatedField(queryset=Pais.objects.all())

  class Meta:
    model = Empleado
    fields = ['__all__']

class PaisSerializer(serializers.Serializer):
  IdPais = serializers.IntegerField()
  Nombre = serializers.CharField(max_length=40)

  class Meta:
    model = Pais
    fields = ['__all__']
  
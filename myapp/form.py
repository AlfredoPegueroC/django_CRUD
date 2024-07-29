from .models import Empleado
from django import forms


class EmpleadoForm(forms.ModelForm):
  class Meta:
    model = Empleado
    fields = ['Nombre','LimiteCredito', 'Pais']
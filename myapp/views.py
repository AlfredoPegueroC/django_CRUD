from django.shortcuts import render, redirect
from .models import Empleado, EmpleadoSerializer, PaisSerializer, Pais
from .form import EmpleadoForm

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
def index(request):
  return render(request, 'client/index.html', {'data': Empleado.objects.all()})

def create(request):
  if request.method == 'POST':
    form = EmpleadoForm(request.POST)
    if form.is_valid():
      form.save()
  return render(request, 'create.html')

def detalle(request, pk):
  emp = Empleado.objects.filter(id=pk).first()
  return render(request, 'detalle.html', {'data': emp})

def update(request, pk):
  emp = Empleado.objects.filter(id=pk).first()
  if request.method == 'POST':
    form = EmpleadoForm(request.POST, instance=emp)
    if form.is_valid():
      form.save()
  else:
   form = EmpleadoForm(instance=emp)
  return render(request, 'update', {'form': form})

def delete(request, pk):
  emp = Empleado.objects.filter(id=pk).first()

  if request.method == 'GET':
    emp.delete()
    return redirect('index')
  
  return render(request, 'delete.html', {'data': emp})

@api_view(['GET'])
def getAllEmpleado(request):
  list = Empleado.objects.all()
  ser = EmpleadoSerializer(list, many=True)
  return Response(ser.data)

@api_view(['GET'])
def getAllPais(request):
  list = Pais.objects.all()
  ser = PaisSerializer(list, many=True)
  return Response(ser.data)
from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator
from .models import Empleado, EmpleadoSerializer, PaisSerializer, Pais
from .form import EmpleadoForm


from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
def index(request):
  emp = Empleado.objects.all()
  paginator = Paginator(emp, 10)

  pageNumber = request.GET.get('page')
  pageObj = paginator.get_page(pageNumber)
  return render(request, 'client/index.html', {'data': pageObj})

#
def create(request):
  if request.method == 'POST':
    form = EmpleadoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = EmpleadoForm()
  return render(request, 'client/create.html', {'form': form})

def detalle(request, pk):
  emp = Empleado.objects.filter(id=pk).first()
  return render(request, 'client/detalle.html', {'data': emp})

def update(request, pk):
  emp = Empleado.objects.filter(id=pk).first()
  if request.method == 'POST':
    form = EmpleadoForm(request.POST, instance=emp)
    if form.is_valid():
      form.save()
    return redirect('index')
  else:
   form = EmpleadoForm(instance=emp)
  return render(request, 'client/update.html', {'form': form})

def delete(request, pk):
  if request.method == 'GET':
    Empleado.objects.filter(id=pk).first().delete()
    return redirect('index')
  return HttpResponse('Deleted Successfully')

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
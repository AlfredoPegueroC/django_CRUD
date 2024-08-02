from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator
from .models import Empleado, EmpleadoSerializer, PaisSerializer, Pais
from .form import EmpleadoForm
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# LISTADO DE CLIENTE
def index(request):
  emp = Empleado.objects.all()
  # PAGINATION TAKES ALL CLIENT AS FIRST PARAM AND AS SECOND PARAM THE NUMBER OF ELEMENT SHOW PER PAGE
  paginator = Paginator(emp, 10)
  # NUMBER OF PAGES, REQUEST.GET.get('page'), 'page' IS GOING TO BE THE REFERENCE ?page=(current-page)
  pageNumber = request.GET.get('page')
  pageObj = paginator.get_page(pageNumber)
  return render(request, 'client/index.html', {'data': pageObj})

# AGREGAR CLIENTE
def create(request):
  print(request.POST)
  if request.method == 'POST':
    form = EmpleadoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    # INITIALIZER EmpleadoForm,THEN FORM.AS_P CAN WORK  
    form = EmpleadoForm()
  data = {'msg': 'registro guardado2', 'form': form}
  return render(request, 'client/create.html', data)

# DETALLE DE CLIENTE
def detalle(request, pk):
  emp = Empleado.objects.filter(id=pk).first()
  return render(request, 'client/detalle.html', {'data': emp})


# ACTUALIZAR CLIENTE
def update(request, pk):
  emp = Empleado.objects.filter(id=pk).first()
  if request.method == 'POST':
    # INSTANCE = EMPLEADO FILL ALL INPUT WITH THE DATA FROM DATA BASE.
    form = EmpleadoForm(request.POST, instance=emp)
    if form.is_valid():
      form.save()
    return redirect('index')
  else:
   form = EmpleadoForm(instance=emp)
  return render(request, 'client/update.html', {'form': form})

# BORRAR CLIENTE
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
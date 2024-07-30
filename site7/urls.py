"""
URL configuration for site7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('myapp/create', views.create, name='create'),
    path('myapp/detalle/<int:pk>/', views.detalle, name='detalle'),
    path('myapp/update/<int:pk>', views.update, name='update'),
    path('myapp/delete/<int:pk>', views.delete, name='delete'),
    path('myapp/data/empleado', views.getAllEmpleado),
    path('myapp/data/pais', views.getAllPais)
]

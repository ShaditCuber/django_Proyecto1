"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Proyecto1.views import saludar,segunda_vista,dia_de_hoy,mi_nombre_es,calcular_año_nacimiento,probando_template # Lo creamos nosotros E IMPORTAR SOLO LAS NECESARIASS
#o from Proyecto1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    #lo agregamos nosotros desde aqui
    path('saludo/', saludar,name='saludar'),
    path('segundavista', segunda_vista,name='segunda_vista'), 
    path('diadehoy', dia_de_hoy,name='dia_de_hoy'),
    path('minombrees/<name>', mi_nombre_es,name='mi_nombre_es'),
    path('calcularanonacimiento/<edad>', calcular_año_nacimiento,name='calcular_año_nacimiento'),
    path('probandotemplate', probando_template,name='probando_template'),
]

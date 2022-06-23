#NOSOTROS CREAMOS ESTE ARCHIVO PARA QUE PUEDA HACER LOS CONTROLADORES DE NUESTRA APLICACION
from pipes import Template
from django.http import HttpResponse

#importamos datetime
from django.template import Context, Template
import datetime


def saludar(request):
    return HttpResponse("Hola mundo!!")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendi !!")

def dia_de_hoy(request):
    return HttpResponse("<br><br>Hoy es: " + str(datetime.datetime.today()))

def mi_nombre_es(request,name):
    return HttpResponse("<br><br>Mi nombre es: <b>"+name+"<b>")

def calcular_año_nacimiento(request,edad):
    return HttpResponse("<br><br>Tu año de nacimiento es: <b>" + str(datetime.datetime.today().year - int(edad))+"<b>")

def probando_template(request):
   miHtml= open('C:/Users/Felipe Ignacio/Desktop/DJANGO/Proyecto1/plantillas/template.html')
   plantilla = Template(miHtml.read())
   miHtml.close()
   miContexto = Context()
   documento= plantilla.render(miContexto)
   return HttpResponse(documento)

    
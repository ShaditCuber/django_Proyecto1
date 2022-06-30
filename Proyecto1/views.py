#NOSOTROS CREAMOS ESTE ARCHIVO PARA QUE PUEDA HACER LOS CONTROLADORES DE NUESTRA APLICACION
from pipes import Template
from django.http import HttpResponse
#PARA CARGAR VARIAS PLANTILLAS
from django.template import loader

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
   #creamos variables para un diccionario
   nombre =" Felipe"
   apellido="Bastidas"
   fecha = datetime.datetime.now()
   lista_de_notas=[2,2,3,7,2,5]
   #creamos diccionario
   diccionario = {'nombre':nombre,'apellido':apellido,'fecha':fecha,'notas':lista_de_notas}
   '''miHtml= open('C:/Users/Felipe Ignacio/Desktop/DJANGO/Proyecto1/plantillas/template.html')
   plantilla = Template(miHtml.read())
   miHtml.close()
   #lo agregamos al contexto
   miContexto = Context(diccionario)
   documento= plantilla.render(miContexto)'''
   #cargamos la plantilla
   plantilla = loader.get_template('template.html')
   documento = plantilla.render(diccionario)
   return HttpResponse(documento)

    
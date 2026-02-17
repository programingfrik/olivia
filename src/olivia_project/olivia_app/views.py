# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Persona

# Create your views here.

def index(request, usuario_id = None):
    contactos = Persona.objects.order_by("nacimiento")
    #salida = ", ".join([p.nombres + " " + p.apellidos for p in contactos])
    #return HttpResponse(salida)
    template = loader.get_template("olivia_app/index.html")
    context = {"contactos": contactos}
    return HttpResponse(template.render(context, request))

def detalle_cont(request, usuario_id = None, contacto_id = None):
    return HttpResponse("Este es el detalle de un contacto %s. Que es un contacto de %s." % (contacto_id, usuario_id))

# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request, usuario_id = None):
    return HttpResponse("Este es el indice de contactos %s." % usuario_id)

def detalle_cont(request, usuario_id = None, contacto_id = None):
    return HttpResponse("Este es el detalle de un contacto %s. Que es un contacto de %s." % (contacto_id, usuario_id))

# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hola Edmundo. Estas en el indice de olivia la agenda de contactos de la nueva generación")

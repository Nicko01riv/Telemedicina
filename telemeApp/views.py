from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def inicio(request):
    return HttpResponse("<h1>´Pagina Inicial de telemeApp<h1>")

def ahora(request):
    hora = datetime.datetime.now()
    salida = "<b>Fecha y hora actual: {}</b>".format(hora)
    return HttpResponse(salida) 
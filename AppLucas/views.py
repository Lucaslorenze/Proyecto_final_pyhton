from multiprocessing import reduction
from django.shortcuts import render
from django.http import HttpResponse
from AppLucas.models import Familiar

# Create your views here.

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def saludo_dos(request):
    return HttpResponse("Que ondaaaaa")

def mostrar_mi_template(request):
    return render(request, "AppLucas/index.html", 
    {
        "nombre":"Lucas",
        "apellido":"Lorenzo"
        })

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "AppLucas/familiares.html", {"lista_familiares": lista_familiares}) # Esto se llama contexto
  
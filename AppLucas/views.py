from multiprocessing import reduction
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

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
def fecha(request):
    fecha_actual = date.today()
    return fecha_actual
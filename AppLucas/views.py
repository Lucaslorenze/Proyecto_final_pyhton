from multiprocessing import reduction
from django.shortcuts import render
from django.http import HttpResponse
from AppLucas.models import Familiar
from AppLucas.forms import Buscar, FamiliarForm
from django.views import View

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


class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'AppLucas/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'AppLucas/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})


from django.contrib import admin
from django.urls import path
from AppLucas.views import mostrar_mi_template, saludo, saludo_dos, monstrar_familiares, BuscarFamiliar, AltaFamiliar
from blog.views import index as blog_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("test/",saludo),
    path("test2/",saludo_dos),
    path("template/",mostrar_mi_template),
    path('mi-familia/', monstrar_familiares),
    path("blog/", blog_index),
    path("mi-familia/buscar", BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view())
]

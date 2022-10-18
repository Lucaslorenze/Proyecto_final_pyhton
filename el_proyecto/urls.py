"""el_proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppLucas.views import mostrar_mi_template, saludo, saludo_dos, imc

urlpatterns = [
    path('admin/', admin.site.urls),
    path("test/",saludo),
    path("test2/",saludo_dos),
    path("template/",mostrar_mi_template),
    path("indice de masa corporal/<peso>/<altura>",imc)
]
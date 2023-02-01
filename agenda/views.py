from django.shortcuts import render, get_list_or_404
from django.template import loader
from .models import Empresa

def listado(request):
     empresas = get_list_or_404(Empresa)
     contexto = {
          'empresas': empresas,
     }
     template = 'agenda/lista.html'
     return render(request, template, contexto)
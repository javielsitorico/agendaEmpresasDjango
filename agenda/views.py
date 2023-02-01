from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.template import loader
from django.views.generic import ListView, DetailView
from .models import Empresa

class EmpresaListView(ListView):
     model = Empresa
     # context_object_name = 'empresas'
     
class EmpresaDetailView(DetailView, ):
     model = Empresa

# Esta seria la manera de hacerlo que conocemos
#
# def listado(request):
#      empresas = get_list_or_404(Empresa)
#      contexto = {
#           'empresas': empresas,
#      }
#      template = 'agenda/lista.html'
#      return render(request, template, contexto)
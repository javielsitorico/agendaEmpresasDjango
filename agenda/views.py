from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.template import loader
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Empresa

class EmpresaListView(ListView):
     model = Empresa
     # context_object_name = 'empresas'
     
class EmpresaDetailView(DetailView):
     model = Empresa
     
class EmpresaCreateView(CreateView):
     model = Empresa
     fields = ['nombre', 'tipo', 'direccion', 'telefono', 'personaContacto']
     success_url = reverse_lazy('listado')

class EmpresaUpdateView(UpdateView):
     model = Empresa
     fields = ['nombre', 'tipo', 'direccion', 'telefono', 'personaContacto']
     template_name_suffix = '_update'
     success_url = reverse_lazy('listado')

class EmpresaDeleteView(DeleteView):
     model = Empresa
     success_url = reverse_lazy('listado')


# Esta seria la manera de hacerlo que conocemos
#
# def listado(request):
#      empresas = get_list_or_404(Empresa)
#      contexto = {
#           'empresas': empresas,
#      }
#      template = 'agenda/lista.html'
#      return render(request, template, contexto)
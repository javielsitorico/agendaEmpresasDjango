from django.urls import path, include
from . import views

urlpatterns = [
     path('', views.EmpresaListView.as_view(), name='listado'),
     path('empresa/<int:pk>', views.EmpresaDetailView.as_view(), name='detalle'),
     path('crear', views.EmpresaCreateView.as_view(), name='crear'),
     path('modificar/<int:pk>', views.EmpresaUpdateView.as_view(), name='modificar'),
     path('borrar/<int:pk>', views.EmpresaDeleteView.as_view(), name='borrar'),
]
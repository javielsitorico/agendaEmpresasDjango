from django.urls import path, include
from . import views

urlpatterns = [
     path('', views.EmpresaListView.as_view(), name='listado'),
     path('empresa/<int:pk>', views.EmpresaDetailView.as_view(), name='detalle'),
]
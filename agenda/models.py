from django.db import models

class Empresa(models.Model):
     nombre = models.CharField(max_length=256)
     tipo = models.CharField(max_length=256)
     direccion = models.CharField(max_length=256)
     telefono = models.CharField(max_length=256)
     personaContacto = models.CharField(max_length=256)
     created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
     updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de modificación')
     
     def __str__(self):
        return self.nombre
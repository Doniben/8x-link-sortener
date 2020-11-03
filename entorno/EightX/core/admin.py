from django.contrib import admin
from .models import Enlace
# Se usa un decorador y se le pasa el modelo de enlace
# Se crea una clase 
# Se pasa la propiedad pass

@admin.register(Enlace)
class Administrador(admin.ModelAdmin):
    pass
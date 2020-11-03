"""EightX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

# Se crea una nueva función llamada include. Por ella se crea un nuevo path
# El path es una dirección que coincide tanto en el navegador como con la que se crea dentro del archivo url
# Al ser iguales se ejecuta la función que se le indica, es decir la vista.
# Se crea un path con dirección raíz con la función include, indicándole en dǿnde estarán las otras direcciones que coincidirán con la dirección raíz.
#


urlpatterns = [
    path('', include('core.urls')),
    path('a/admin/', admin.site.urls),
]

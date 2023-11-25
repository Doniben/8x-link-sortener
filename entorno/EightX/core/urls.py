from django.urls import path
from .views import CrearAcortador, paginaEnlace, RedirectEnlace, set_session, get_session

# Se usa la propiedad app_name para identificar las redirecciones que se crean dentro de cada aplicaciǿn de forma legible,
# evitando confuciones cuando tenemos muchas aplicaciones.
# Luego se crea la lista que contendrá cada dirección: Con el path a la raíz + la función clase que queremos que alguien eralice cuando entre al directorio raíz. Es decir, crear el acortador. 
# Puesto que se trata de vistas basadas en clases debemos indicarlo con .as_view() y finalmente el nombre con el que se puede identificar las direcciones en concreto.
# Cuando se trata de tipos de datos dinámicos dentro de la dirección dentro de la url se pone entre signos <>, con el tipo de dato que se espera, dos puntos y el nombre esperado.
# Página enlace que es la vista detalle
# en la función ge_absolute_ur, dentro de los modelos estamos redirigiendo ala vista de detalle
# Para la última dirección se espera un código de tipo string con la función Redirect
app_name = 'core'
urlpatterns = [
    path('set_session/', set_session, name='set_session'),
    path('get_session/', get_session, name='get_session'),
    path('', CrearAcortador.as_view(), name='inicio'),
    path('<int:pk>/', paginaEnlace.as_view(), name='detalle'),
    path('8/<str:codigo>/', RedirectEnlace.as_view(), name='redirect'),
]
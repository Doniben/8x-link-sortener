
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView
from .forms import AcortadorForm
from .models import Enlace

# Se crea la primera vista y se hereda de CreateView y se le pasan 3 propiedades
# asignamos el Enlace
# asignamos el formulario creado de forma personalizada (AcortadorForm)
# Y el archivo en el que se renderizará la vista ()

# Esta vista tiene un método  que contiene el contexto original sin editar con el diccionario de **kwargs. La función Genera todo lo que se visualizará en el .html.
# rederizará cada elemento que se envía en forma de diccionario. Para general diccionarios se pasa tanto la clave como su valor
# Se generan otros dos contextos que se generan en la lógica de los modelos: 1. contados de enlaces; 2. Contador de redirecciones

class CrearAcortador(CreateView):
    model = Enlace
    forms_class = AcortadorForm
    template_name = 'inicio.html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['total_enlaces'] = Enlace.enlaces.total_enlaces()
        contecto['total_redirecciones'] = Enlace.enlaces.total_redirecciones()['redirecciones']
        return contexto


# Página encargada de renderizar un solo elemento. Se le pasa enlace y la plantilla en la que renderizará
# en esta vista se modificará get_data
# Se crea el contexto original, con la misma funcion
# Se le envía la cantidad de redireciones creadas por fecha.
# En los modelos fecha espera una llava primaria (pk) enviada por el metodo get_absolute_url en core detalle.
# En ccbv la vista DEtailView manera el parámetro pk_url_kwarg = 'pk' por defecto puesto que necesita renderizar algo.
# ese algo es un identificador único en la base de datos, en este caso una primary key.
# Para obtener el valor de las redirecciones que se hicieron en las fechas de Julio se procede en la posicion 0 puesto que
# se trata de un querySet. como estamos filtrando por una llave primera obtenemos por lo tanto una sola posiciǿn, la posición 0 y el valor de julio.



class paginaEnlace(DetailView):
    model = Enlace
    template_name = 'enlace.html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['julio'] = Enlace.enlaces.fechas(self.kwargs['pk'])[0]['julio']


#
class RedirectEnlace():

    def get_redirect_url(self, *args, **kwargs):
        try:
            return Enlace.enlaces.decode_enlace(senlf.kwargs['codigo'])
        except IndexError:
            print("Decode sin datos")
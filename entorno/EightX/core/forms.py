from django import forms
from .models import Enlace

# Se importa forms y el modelo creado "Enlace"
# Se crea el formulario en base al modelo que se ha creado
# Se hereda de forms ModelForms.
# Se crea la clase Meta con el modelo creado, los campos del formulario y los witgets para configurar los estilos.
# Al witgets se le pasan los valores en diccionario: url será la clave y el valor será form.URLInput cuyos atributos vienen en forma de diccionario
# Se trata de atributos HTML para que se renderice con los estilos.

class AcortadorForm(forms.ModelForm):

    class Meta:
        model = Enlace
        fields = ['url']
        widgets = {
            'url': forms.URLInput(attrs={'class': 'input is-rounded is medium', 'placeholder': 'URL to cut'})
        }
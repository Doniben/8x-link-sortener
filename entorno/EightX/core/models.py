from django.db import models
from django.urls import reverse
from hashids import Hashids
import datetime

class EnlaceQuerySet(models.QuerySet):
    # Se decodifica cada código enviado.
    # Se crea variable que almacena llave primaria luego de codificar. Hashids al decodificar devuelve una tupla de un solo elemento.
    # cada decodificación de enlace significa una redirección. Contado almacena cada redirección realizada. Filter es un método creado en la clase QuerySet.
    # Se modifica el campo contador.
    # F es una expresión en Django que permite realizar consultas obtimizadas, pues no realiza la consulta directamen en la bd sino como una referencia.
    # se devuelve la url en sí. Se consulta por la pk.
    # siempre se obtiene el primer elemento porque solo existe una vez en la base de datos. solo nos interesa la url.
    def decode_enlace(self, codigo):
        decode = Hashids(min_length=4, alphabet='abcdefghijklmnopqrstuvwxyz').decode(codigo)[0]
        self.filter(pk=decode).update(contador=models.F('contador') + 1)
        return self.filter(pk=decode).first()

    #Cantidad de enlaces registrados.

    def total_enlaces(self):
        return self.count()

    # Agregaciǿn indica a consulta realizada que se espera una cláusula de suma total del campo contador solicitado para el total de redirecciones realizadas en toda la bd.
    def total_redirecciones(self):
        return self.aggregate(redirecciones=models.Sum('contador'))


# Creando primer modelo: El enlace 
class Enlace(models.Model):
    #Columnas de la tabla Enlace:
    # 1. Se crea el campo de la URL
    # 2. El campo código será el identificador de cada URL registrada, ya acortada. 
    # CharField espera un parámetro obligatorio sobre la máxima cantidad de carácteres del campo (No debe ser menor a la longitud del código)
    # Código será opcional cuando se registra un formulario, puesto que el código lo genera el acortador en base a cada url registrada.
    # Solo usaremos fecha, pero también se puede usar DateTimeField.
    # auto_now_add permitirá registrar una sola vez un solo enlace.
    # Contador almacena cada visita a cada enlace, Numeros positivos desde 0.
    url = models.URLField()
    codigo = models.CharField(max_length=8, blank=True)
    fecha = models.DateField(auto_now_add=True)
    contador = models.PositiveIntegerField(default=0)

    # Sobreescribimos métodos que vienen por defecto al heredar de models

    class Meta:
        verbose_name_plural = 'Enlaces'

    # El método __str__ devuelve una forma más legible de una instancia de un enlace. Puede ser otra instancia de otro modelo(?).
    # El método se crea cuando creamos un nuevo modelo. De no ser así, al realizar una consulta desde la terminal o el administrador aparecería error que no permite identificar los objetos.
    # Para visualizarlo se usará el formato "URL + Código"
    def __str__(self):
        return f"URL: {self.url} Código: {self.codigo}"

    # el método save crea un nuevo objeto dentro de la base de datos cada vez que se le llama.
    # Generamos el código en base a una llave primaria que se genera en cada enlace. Se debe crear justo despues de crearse la llave primaria.
    # En la validación se genera el código y se codifica cada llave primaria que se registra en la base de datos.
    # Se codifica la llave primaria de cada enlace registrado.
    # Django automáticamente declara pk (primary key). Es un identificado único en la bd que se autoincrementa con el registro de cada nuevo elemento
    def save(self, *args, **kwargs):
        super().save(args, **kwargs)
        if not self.codigo:
            self.codigo = Hashids(min_length=4, alphabet='abcdefghijklmnopqrstuvwxyz').encode(self.pk)
            self.save()

    # Crear url en base a un objeto con la función reverse
    def get_absolute_url(self):
        return reverse('core:detalle', kwargs={'pk': self.pk})
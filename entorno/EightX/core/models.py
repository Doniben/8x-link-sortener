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
        return self.filter(pk=decode).first().url

    #Cantidad de enlaces registrados.

    def total_enlaces(self):
        return self.count()

    # Ag gregate indica a consulta realizada que se espera una cláusula de suma total del campo contador solicitado para el total de redirecciones realizadas en toda la bd.
    def total_redirecciones(self):
        return self.aggregate(redirecciones=models.Sum('contador'))

    # el pk se usará para aceptar cada enlace que se le pase.
    # la función values obtiene valores en forma de diccionarios.
    # Se le pasa el campo que se quiere llama, que es fecha en este caso.
    # Annotate es una función como la de aggregate que trabaja sobre cada objeto del querySet aplicando una operación que le indiquemos. Aggregate opera sobre un conjunto del queryset para obtener un valor único, se usó para contar el total de los enlaces.
    # luego identificaremos el valor de noviembre con la cláusula Sum la cual recibe los parámetros del contador (Que cuenta cantidad de redirecciones de una fecha a otr)
    #  y filter con Q, que es para realizar consultas complejas. El primer parámetro de Q es el inicio del contador (filter__gte: >) y 
    #  Cuando ya tenemos nuestra anotación de la fecha de inicio y la fecha final y la suma total de ese rango colocamos un nuevo filtro
    # COn el último filtro se filtra tanto la fecha como el contador por cada enlace que se le pasa a la función fecha.
    # Se queremos escribir más fechas, basta con escribir una , al final de la primera consulta que es noviembre y agregar los siguinetes meses
    def fechas(self, pk):
        return self.values('fecha').annotate(
            noviembre=models.Sum('contador', filter=models.Q(
                fecha__gte=datetime.date(2020, 11, 1), fecha__lte=datetime.date(2020, 11, 30)
                )
                )
            ).filter(pk=pk)

 
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

    # Se indica al queryset que se trata de un administrador para el modelo.

    enlaces = EnlaceQuerySet.as_manager()

    # Sobreescribimos métodos que vienen por defecto al heredar de models

    class Meta:
        verbose_name_plural = 'Enlaces'

    # El método __str__ devuelve una forma más legible de una instancia de un enlace. Puede ser otra instancia de otro modelo(?).
    # El método se crea cuando creamos un nuevo modelo. De no ser así, al realizar una consulta desde la terminal o el administrador aparecería error que no permite identificar los objetos.
    # Para visualizarlo se usará el formato "URL + Código"
    def __str__(self):
        return f"URL: {self.url} codigo: {self.codigo}"

    # el método save crea un nuevo objeto dentro de la base de datos cada vez que se le llama.
    # Generamos el código en base a una llave primaria que se genera en cada enlace. Se debe crear justo despues de crearse la llave primaria.
    # En la validación se genera el código y se codifica cada llave primaria que se registra en la base de datos.
    # Se codifica la llave primaria de cada enlace registrado.
    # Django automáticamente declara pk (primary key). Es un identificado único en la bd que se autoincrementa con el registro de cada nuevo elemento
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.codigo:
            self.codigo = Hashids(min_length=4, alphabet='abcdefghijklmnopqrstuvwxyz').encode(self.pk)
            self.save()

    # Crear url en base a un objeto con la función reverse (modificación del método en el modelo)
    # se le pasan dos parametros: el primero será la ulr a la que se a redirigido una vez creada la instancia, es decir el nuevo enlace. 'detalle'
    # El segundo será es un diccionario 
    def get_absolute_url(self):
        return reverse('core:detalle', kwargs={'pk': self.pk})

    # Trabajando la lógica en un modelo utilizando querySet (pues no hay lógica en vistas, solo se trabaja desde los modelos).

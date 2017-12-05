from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from base.constant import SEXO, ESTADO_CIVIL, TIPO_GACETA
from base.models import Parroquia
from django.contrib.auth.models import User

# Create your models here.

class Persona(models.Model):

    nombre = models.CharField(max_length=100)

    apellido = models.CharField(max_length=100)

    cedula = models.CharField(
        max_length=9,
        help_text=_("Cédula de Identidad del usuario"),
        validators=[
            validators.RegexValidator(
                r'^[VE][\d]{8}$',
                _("Introduzca un número de cédula válido. Solo se permiten números y una longitud de 8 carácteres. Se agrega un 0 si la longitud es de 7 carácteres.")
            ),
        ],unique=True
    )

class RegistradorCivil(models.Model):

    resolucion = models.CharField(max_length=100)

    fecha_resolucion = models.DateField()

    gaceta = models.CharField(max_length=100)

    tipo_gaceta = models.CharField(max_length=1, choices=TIPO_GACETA)

    fecha_gaceta = models.DateField()

    persona = models.ForeignKey(Persona)

    def __str__(self):
        return self.persona.nombre + " " + self.persona.apellido + " " + self.persona.cedula

class Fallecido(models.Model):

    fecha_nacimiento = models.DateField()

    sexo = models.CharField(max_length=1, choices=SEXO)

    edad = models.IntegerField()

    estado_civil = models.CharField(max_length=2, choices=ESTADO_CIVIL)

    profesion = models.CharField(max_length=100)

    ocupacion = models.CharField(max_length=100)

    direccion = models.CharField(max_length=200)

    lugar_nacimiento = models.ForeignKey(Parroquia)

    persona = models.ForeignKey(Persona)

    def __str__(self):
        return self.persona.nombre + " " + self.persona.apellido + " " + self.persona.cedula

class Autoridad(models.Model):

    numero_mpps = models.CharField(max_length=100)

    persona = models.ForeignKey(Persona)

    def __str__(self):
        return self.persona.nombre + " " + self.persona.apellido + " " + self.persona.cedula

class Defuncion(models.Model):

    fecha_hora = models.DateTimeField()

    causa = models.CharField(max_length=200)

    certificado_defuncion = models.CharField(max_length=100)

    lugar = models.ForeignKey(Parroquia)

    direccion = models.CharField(max_length=200)

    autoridad = models.ForeignKey(Autoridad)

    def __str__(self):
        return str(self.fecha_hora) + " " + self.certificado_defuncion

class Pareja(models.Model):

    profesion = models.CharField(max_length=100)

    ocupacion = models.CharField(max_length=100)

    direccion = models.CharField(max_length=200)

    vive = models.BooleanField()

    persona = models.ForeignKey(Persona)

    fallecido = models.ForeignKey(Fallecido)

class Hijo(models.Model):

    vive = models.BooleanField()

    edad = models.IntegerField()

    persona = models.ForeignKey(Persona)

    fallecido = models.ForeignKey(Fallecido)

class Padres(models.Model):

    vive = models.BooleanField()

    edad = models.IntegerField()

    persona = models.ForeignKey(Persona)

    fallecido = models.ForeignKey(Fallecido)

class Declarante(models.Model):

    edad = models.IntegerField()

    profesion = models.CharField(max_length=100)

    ocupacion = models.CharField(max_length=100)

    direccion = models.CharField(max_length=200)

    persona = models.ForeignKey(Persona)

    def __str__(self):
        return self.persona.nombre + " " + self.persona.apellido + " " + self.persona.cedula

class ActaDefuncion(models.Model):

    numero_acta = models.CharField(max_length=10)

    numero_folio = models.CharField(max_length=10)

    anho = models.CharField(max_length=4)

    registrador_civil = models.ForeignKey(RegistradorCivil)

    fallecido = models.ForeignKey(Fallecido)

    #autoridad = models.ForeignKey(Autoridad)

    defuncion = models.ForeignKey(Defuncion)

    #pareja = models.ForeignKey(Pareja)

    #hijo = models.ForeignKey(Hijo)

    #padres = models.ForeignKey(Padres)

    declarante = models.ForeignKey(Declarante)

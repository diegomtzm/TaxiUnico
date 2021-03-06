from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

RESPUESTAS= (
    ('bueno', 'Bueno'),
    ('regular', 'Regular'),
    ('malo', 'Malo'),
)


class Taxi(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    prom_encuestas = models.IntegerField(default=5, validators=[MinValueValidator(0),
                                       MaxValueValidator(10)])
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    cant_personas = models.IntegerField(default=4, choices=[(4,"4"),(7, "7"),(10,"10")])
    placas = models.CharField(max_length=200)
    lista_permisos = models.BooleanField(max_length=200)
    #pregunta1 = models.CharField(max_length=10, choices=RESPUESTAS)
    #pregunta2 = models.CharField(max_length=10, choices=RESPUESTAS)
    #pregunta3 = models.CharField(max_length=10, choices=RESPUESTAS)

# Create your models here.
class Viaje(models.Model):
    tipo_vehiculo = models.CharField(max_length=100)
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    fecha_terminacion = models.DateTimeField(default=datetime.now,blank=True)
    destino = models.CharField(max_length=200)
    origen = models.CharField(max_length=200)
    taxi_fk = models.ForeignKey(Taxi,on_delete=models.CASCADE,related_name='taxi_viaje')
    user_fk = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_viaje')
    costo = models.IntegerField(default=0)
#class TaxiForm(ModelForm):
 #   class Meta:
  #      model = Taxi
   #     fields = ['pregunta1', 'pregunta2', 'pregunta3']

class Boleto(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    user_fk = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class Encuesta(models.Model):
    taxi_fk = models.ForeignKey(Taxi,on_delete=models.CASCADE,related_name='taxi_encuesta')
    user_fk = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_encuesta')
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    pregunta1 = models.CharField(max_length=200)
    pregunta2 = models.CharField(max_length=200)
    pregunta3 = models.CharField(max_length=200)
    promedio = models.DecimalField(default=0,decimal_places=2,max_digits=100)

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from datetime import datetime

RESPUESTAS= (
    ('bueno', 'Bueno'),
    ('regular', 'Regular'),
    ('malo', 'Malo'),
)

class Taxi(models.Model):
    prom_encuestas = models.IntegerField(default=0)
    t_nombre = models.CharField(max_length=200)
    t_apellido = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    placas = models.CharField(max_length=200)
    lista_permisos = models.BooleanField(max_length=200)
    #pregunta1 = models.CharField(max_length=10, choices=RESPUESTAS)
    #pregunta2 = models.CharField(max_length=10, choices=RESPUESTAS)
    #pregunta3 = models.CharField(max_length=10, choices=RESPUESTAS)

    def __str__(self):
        return self.t_nombre

# Create your models here.
class Viaje(models.Model):
    tipo_vehiculo = models.CharField(max_length=100)
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    destino = models.CharField(max_length=200)
    origen = models.CharField(max_length=200)
    taxi_fk = models.ForeignKey(Taxi,on_delete=models.CASCADE)
    user_fk = models.ForeignKey(User,on_delete=models.CASCADE)
    costo = models.IntegerField(default=0)
#class TaxiForm(ModelForm):
 #   class Meta:
  #      model = Taxi
   #     fields = ['pregunta1', 'pregunta2', 'pregunta3']

class Boleto(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    user_fk = models.ForeignKey(User,on_delete=models.CASCADE)

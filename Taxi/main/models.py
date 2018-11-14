from django.db import models
from django.contrib.auth.models import User

class Taxi(models.Model):
    prom_encuestas = models.IntegerField(default=0)
    t_nombre = models.CharField(max_length=200)
    t_apellido = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    placas = models.CharField(max_length=200)
    lista_permisos = models.BooleanField(max_length=200)

# Create your models here.
class Viaje(models.Model):
    tipo_vehiculo = models.CharField(max_length=100)
    fecha = models.DateTimeField('date published')
    destino = models.CharField(max_length=200)
    origen = models.CharField(max_length=200)
    taxi_fk = models.ForeignKey(Taxi,on_delete=models.CASCADE)
    user_fk = models.ForeignKey(User,on_delete=models.CASCADE)

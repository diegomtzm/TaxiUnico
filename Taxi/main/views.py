from django.shortcuts import render
from .models import Viaje
from django.contrib.auth.models import User
import config

viajes = [
    {
        'fecha' : 'OCT 07 2018 - 8:30 AM',
        'origen' : 'Tecnologico de Mty',
        'destino' : 'Estacion Autobus Mty',
        'costo' : '100.00',
    },
    {
        'fecha' : 'OCT 10 2018 - 12:30 PM',
        'origen' : 'Soriana Centro Saltillo',
        'destino' : 'Estacion Autobus Saltillo',
        'costo' : '90.00',
    },
    {
        'fecha' : 'OCT 15 2018 - 10:30 PM',
        'origen' : 'Estacion San Luis Potosi',
        'destino' : 'Calle Mirador, #240, Col.',
        'costo' : '54.00',
    }
]

user = {
    'nombre' : 'Hector',
    'apellido' : 'De Luna',
    'edad' : 21,
    'viajes' : 341,
}

# Create your views here.
def home(request):
    username = None
    if request.user.is_authenticated:
        username = request.user

    context = {
        'user' : username,
        'api' : config.api_key
    }
    return render(request, 'main/index.html',context)

def reservas(request):
    context = {
        'viajes' : Viaje.objects.filter(user_fk=request.user.id)
    }
    return render(request,'main/reservas.html',context)

def historial(request):
    context = {
        'viajes' : Viaje.objects.filter(user_fk=request.user.id)
    }
    return render(request,'main/historial.html',context)

def perfil(request):
    context = {
        'user' : user
    }
    return render(request,'main/perfil.html',context)
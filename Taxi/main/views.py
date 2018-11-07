from django.shortcuts import render

viajes = [
    {
        'fecha' : 'OCT 07 2018 - 8:30 AM',
        'origen' : 'Tecnologico de Mty',
        'destino' : 'Estacion Autobus Mty',
        'costo' : '65.00',
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

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def reservas(request):
    context = {
        'viajes' : viajes
    }
    return render(request,'main/reservas.html',context)

def historial(request):
    context = {
        'viajes' : viajes
    }
    return render(request,'main/historial.html',context)
from django.shortcuts import render, redirect
from .models import Viaje
from main.forms import TaxiForm
from django.contrib import messages
from django.shortcuts import render
from .models import Viaje, Taxi
from .models import Boleto
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
User = get_user_model()
import config
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime, timezone
import math
from .decorators import taxi_required
from .forms import UserRegisterForm

@login_required
# Create your views here.
def home(request):
    username = None
    if request.user.is_authenticated:
        username = request.user

    form = TaxiForm()

    context = {
        'user' : username,
        'api' : config.api_key,
        'taxista' : Taxi.objects.first(),
        'form' : form
    }
    return render(request, 'main/index.html',context)
'''
VIAJES
'''
@login_required
def reservas(request):
    context = {
        'viajes' : Viaje.objects.filter(user_fk=request.user.id)
    }
    return render(request,'main/reservas.html',context)

@login_required
def historial(request):
    context = {
        'viajes' : Viaje.objects.filter(user_fk=request.user.id)
    }
    return render(request,'main/historial.html',context)

class ViajeListView(ListView):
    model = Viaje
    template_name = 'main/historial.html'
    context_object_name = 'viajes'
    ordering = ['-fecha']

class ViajeDetailView(DetailView):
    model = Viaje


'''
USUARIO

class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = ['first_name','last_name','email']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        user = selft.get_object()
        if self.request.user == user.id:
            return True
        return false
'''
@login_required
def perfil(request):
    username = None
    if request.user.is_authenticated:
        username = request.user

    context = {
        'user' : username
    }
    return render(request,'main/perfil.html',context)

@login_required
def encuesta(request):
    if request.method == 'POST':
        form = TaxiForm(request.POST)
        if form.is_valid():
            messages.success(request, f'Gracias por contestar la encuesta!')
            return redirect('home-main')
    else:
        form = TaxiForm()
    return render(request, 'main/encuesta.html', {'form': form})

@login_required
def boletos(request):
    context = {
        'boletos' : Boleto.objects.filter(user_fk=request.user.id)
    }

    return render(request,'main/boletos.html',context)


'''
AJAX
'''
def pedir_taxi(request):
    username = None
    if request.user.is_authenticated:
        username = request.user

    taxi = Taxi.objects.order_by("?").first()

    origen_user = request.GET.get('origen',None)
    destino_user = request.GET.get('destino',None)

    viaje_usuario = Viaje.objects.create(origen=origen_user,destino=destino_user,user_fk=username,costo=0,taxi_fk=taxi)



    data = {
        'nombre' : taxi.user.first_name,
        'apellido' : taxi.user.last_name,
        'modelo' : taxi.modelo,
        'marca' : taxi.marca,
        'placas' : taxi.placas,
        'viaje_id' : viaje_usuario.id,
        'taxi_id' : taxi.id
    }

    return JsonResponse(data)

def acabar_viaje(request):
    username = None
    if request.user.is_authenticated:
        username = request.user

    # obtiene el id de un AJAX post request
    viaje = request.GET.get('viaje_id',None)

    # filtra los viajes con el id y lo toma de la base de datos
    viaje_usuario = Viaje.objects.get(id=viaje)
    # guarda el momento que se acabo el viaje
    viaje_usuario.fecha_terminacion = datetime.now(timezone.utc)

    # obtiene la diferencia del tiempo
    timediff = viaje_usuario.fecha_terminacion.timestamp() - viaje_usuario.fecha.timestamp()
    # calcula el costo total
    costo_total = math.floor(timediff * 0.8)
    # guarda el costo
    viaje_usuario.costo = costo_total

    # guarda todos los cambios
    viaje_usuario.save()

    data = {
        'costo' : costo_total
    }

    return JsonResponse(data)


# Signup
def signup(request):
    if request.method == 'POST':
        form_class = UserRegisterForm(request.POST)
        if form_class.is_valid():
            form_class.save()
            username = form_class.cleaned_data.get('username')
            messages.success(request, f'Tu cuenta se a registrado!')
            return redirect('home-main')

    else:
        form_class = UserRegisterForm

    return render(request,'main/signup.html',{'form' : form_class })
# Views for the taxi driver
@taxi_required
def taxi(request):
    username = None
    if request.user.is_authenticated:
        username = request.user

    context = {
        'user' : username
    }
    return render(request, 'main/taxi-main.html', context)
@taxi_required
def taxi_viaje(request):
    context = {
        'api' : config.api_key
    }
    return render(request, 'main/taxi-viaje.html',context)
@taxi_required
def taxi_historial(request):
    context = {
        'viajes' : Viaje.objects.filter(user_fk=request.user.id)
    }
    return render(request,'main/taxi-historial.html',context)
@taxi_required
def taxi_perfil(request):
    username = None
    if request.user.is_authenticated:
        username = request.user

    context = {
        'user' : username
    }
    return render(request,'main/taxi-perfil.html',context)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Encuesta
from datetime import datetime


RESPUESTAS= (
    ('bueno', 'Bueno'),
    ('regular', 'Regular'),
    ('malo', 'Malo'),
)

class TaxiForm(forms.ModelForm):
    user_fk = forms.IntegerField(required=False,widget=forms.HiddenInput())
    taxi_fk = forms.IntegerField(required=False,widget=forms.HiddenInput())
    promedio = forms.DecimalField(required=False,decimal_places=2,widget=forms.HiddenInput())
    fecha = forms.DateTimeField(initial=datetime.now(), required=False,widget=forms.HiddenInput())
    pregunta1= forms.CharField(label='¿Como califica el tiempo de llegada del servicio?', widget=forms.Select(choices=RESPUESTAS))
    pregunta2= forms.CharField(label='¿Como califica la atencion del conductor?', widget=forms.Select(choices=RESPUESTAS))
    pregunta3= forms.CharField(label='¿Como califica la limpieza del vehículo?', widget=forms.Select(choices=RESPUESTAS))

    class Meta:
        model = Encuesta
        fields = ('pregunta1','pregunta2','pregunta3', 'user_fk', 'taxi_fk','fecha','promedio',)
        widgets = {'user_fk': forms.HiddenInput(), 'taxi_fk' : forms.HiddenInput()}

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


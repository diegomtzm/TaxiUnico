from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-main'),
    path('reservas', views.reservas, name='reservas-main'),
    path('historial', views.historial, name='historial-main'),
    path('perfil', views.perfil, name='perfil-main'),
    path('encuesta', views.encuesta, name='encuesta-main'),
    path('boletos', views.boletos, name='boletos-main'),
]

from django.urls import path
from .views import ViajeListView, ViajeDetailView
from . import views

urlpatterns = [
    path('', views.home, name='home-main'),
    path('reservas', views.reservas, name='reservas-main'),
    path('historial', ViajeListView.as_view(), name='historial-main'),
    path('viaje/<int:pk>/', ViajeDetailView.as_view(), name='viaje-detail'),
    path('perfil', views.perfil, name='perfil-main'),
    path('encuesta', views.encuesta, name='encuesta-main'),
    path('boletos', views.boletos, name='boletos-main'),
    path('ajax/pedir_taxi', views.pedir_taxi, name='pedir_taxi'),
]

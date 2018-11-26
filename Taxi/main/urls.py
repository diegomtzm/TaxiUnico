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
    path('ajax/acabar_viaje', views.acabar_viaje, name='acabar_viaje'),
<<<<<<< HEAD
    path('accounts/signup/', views.signup, name='signup'),

=======
    path('taxi', views.taxi, name='taxi-main'),
    path('taxi/viaje', views.taxi_viaje, name='taxi-viaje'),
    path('taxi/historial', views.taxi_historial, name='taxi-historial'),
    path('taxi/perfil', views.taxi_perfil, name='taxi-perfil'),
>>>>>>> ccd7701d8f8faf460b166a23ba635591c218403e
]

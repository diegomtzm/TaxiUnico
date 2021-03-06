from django.urls import path
from .views import ViajeListView, ViajeDetailView, EncuestaListView, EncuestaDetailView
from . import views
from django.contrib.auth import views as auth_views

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
    path('accounts/signup/', views.signup, name='signup'),

    path('taxi', views.taxi, name='taxi-main'),
    path('taxi/viaje', views.taxi_viaje, name='taxi-viaje'),
    path('taxi/historial', views.taxi_historial, name='taxi-historial'),
    path('taxi/perfil', views.taxi_perfil, name='taxi-perfil'),


    path('perfil/actualiza', views.perfil_actualiza, name='perfil-actualiza'),
    
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='main/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='main/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password_reset_complete.html'), name='password_reset_complete'),

    path('taxi/encuesta', EncuestaListView.as_view(), name='taxi-encuesta-main'),
    path('taxi/encuesta/<int:pk>/', EncuestaDetailView.as_view(), name='taxi-encuesta-detail'),

]

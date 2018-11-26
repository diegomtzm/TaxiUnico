from django.contrib import admin
from .models import Viaje
from .models import Taxi
from .models import Boleto
from .models import Encuesta


admin.site.register(Viaje)
admin.site.register(Taxi)
admin.site.register(Boleto)
admin.site.register(Encuesta)
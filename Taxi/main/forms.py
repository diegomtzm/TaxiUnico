from django import forms


RESPUESTAS= (
    ('bueno', 'Bueno'),
    ('regular', 'Regular'),
    ('malo', 'Malo'),
)

class TaxiForm(forms.Form):
    pregunta1= forms.CharField(label='¿Como califica el tiempo de llegada del servicio?', widget=forms.Select(choices=RESPUESTAS))
    pregunta2= forms.CharField(label='¿Como califica la atencion del conductor?', widget=forms.Select(choices=RESPUESTAS))
    pregunta3= forms.CharField(label='¿Como califica la limpieza del vehículo?', widget=forms.Select(choices=RESPUESTAS))
from django import forms
from .models import Paciente, Consulta
from django.forms import Textarea


class AltaPaciente(forms.ModelForm):

    SI = (('No', 'No'), ('Si', 'Si'))
    SEXOS = (('Femenino', 'Femenino'), ('Masculino', 'Masculino'))
    SINO = (('No', 'No'), ('Si', 'Si'), ('Ultimo Año', 'Ultimo Año'), ('Mas de 1 Año', 'Mas de 1 Año'))
    DiabOps = (('No', 'No'), ('Sin Insulina', 'Sin Insulina'), ('Con Insulina', 'Con Insulina'))
    AlimOps = (('Mala', 'Mala'), ('Regular', 'Regular'), ('Buena', 'Buena'))
    Sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=SEXOS)
    Psicologo = forms.ChoiceField(widget=forms.RadioSelect, choices=SINO)
    Pareja = forms.ChoiceField(widget=forms.RadioSelect, choices=SI)
    Constelaciones = forms.ChoiceField(widget=forms.RadioSelect, choices=SINO)
    Yoga = forms.ChoiceField(widget=forms.RadioSelect, choices=SINO)
    OtrosSistemas = forms.ChoiceField(widget=forms.RadioSelect, choices=SI, label="Otros Sistemas")
    Anemia = forms.ChoiceField(widget=forms.RadioSelect, choices=SI)
    Diabetes = forms.ChoiceField(widget=forms.RadioSelect, choices=DiabOps)
    Alimentacion = forms.ChoiceField(widget=forms.RadioSelect, choices=AlimOps)

    class Meta:
        model = Paciente
        fields = '__all__'

class NuevaConsulta(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = ('Observaciones', 'Receta',)
        widgets = {
            'Observaciones': Textarea(attrs={'cols': 128, 'rows': 20}),
        }
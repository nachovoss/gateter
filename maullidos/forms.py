from django import forms
from .models import Maullido

class MaullidoForm(forms.ModelForm):
    class Meta:
        model = Maullido
        fields = ['contenido']

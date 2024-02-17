from django import forms
from .models import Persona

class PersonasForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

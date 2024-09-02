from django import forms
from .models import Formulario

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['nome', 'endereco', 'cidade', 'email', 'curso'] 
        #posso usar o '__all__' também

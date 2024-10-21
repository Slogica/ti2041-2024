from django import forms
from .models import Productos

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'precio', 'tamaño', 'peso', 'categoria', 'marca']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'inputR'}),
            'precio': forms.NumberInput(attrs={'class': 'inputR'}),
            'peso': forms.NumberInput(attrs={'class': 'inputR'}),
            'tamaño': forms.Select(attrs={'class': 'inputR'}),
            'categoria': forms.Select(attrs={'class': 'inputR'}),
            'marca': forms.Select(attrs={'class': 'inputR'}),
        }
from django import forms
from django.core.validators import RegexValidator
from . import models

class RegistrationForm(forms.ModelForm):
    # Defina o validador de telefone
    telephone = forms.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\(\d{2}\) \d{4,5}-\d{4}$',
                message='Número de telefone deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX'
            )
        ],
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Telefone'
    )

    class Meta:
        model = models.CustomerRegistration
        fields = ['name', 'enterprise', 'telephone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'enterprise': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nome',
            'enterprise': 'Empresa',
        }

from django.db import models
from django.core.validators import RegexValidator


class CustomerRegistration(models.Model):
    name = models.CharField(max_length=500)
    enterprise = models.CharField(max_length=500)
    telephone = models.CharField(
        max_length=20,
        validators=[RegexValidator(
            regex=r'^\(\d{2}\) \d{4,5}-\d{4}$',
            message='Número de telefone deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX'
        )]
    )
    
    
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

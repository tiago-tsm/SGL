from django.db import models
from registration.models import CustomerRegistration
from products.models import Product

class Orders(models.Model):
    FORMA_PAGAMENTO_CHOICES = [
        ('dinheiro', 'Dinheiro'),
        ('cartao', 'Cartão'),
        ('aprazo', 'A Prazo'),
    ]
    
    cliente = models.ForeignKey(CustomerRegistration, on_delete=models.CASCADE, related_name='pedidos')
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)  # Ajustado para PositiveIntegerField
    forma_pagamento = models.CharField(max_length=10, choices=FORMA_PAGAMENTO_CHOICES)
    total_compra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data_hora_registro = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        # Verifica se produto e quantidade são válidos
        if self.produto and self.quantidade >= 0:
            self.total_compra = self.produto.selling_price * self.quantidade
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return f'Pedido {self.id} - {self.cliente}'

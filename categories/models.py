from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # Registra data atual, daquele momenmto 
    update_at = models.DateField(auto_now=True) #Atualiza para data que esta sendo modificado 
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name

from django.db import models

# Create your models here.


class Formulario(models.Model):
    nome= models.CharField(max_length=150)
    endereco= models.CharField(max_length=100)
    cidade= models.CharField(max_length=70)
    email= models.EmailField()
    curso= models.CharField(max_length=70)
    
    def __str__(self):
        return self.nome
    
    
    
    
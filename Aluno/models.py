from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True)
    idade = models.IntegerField(null=True)
    curso = models.CharField(max_length=50, null=True)
    altura = models.CharField(max_length=5, null=True )
    def __str__(self):
        return self.nome
    
class Interesses(models.Model):
    nome = models.OneToOneField(Aluno, on_delete=models.CASCADE)
    descricao = models.TextField()
    
    def __str__(self):
        return self.descricao
from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True)
    idade = models.IntegerField(null=True)
    curso = models.CharField(max_length=50, null=True)
    altura = models.CharField(max_length=5, null=True )
    #curso = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
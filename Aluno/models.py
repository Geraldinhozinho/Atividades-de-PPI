from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    #curso = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
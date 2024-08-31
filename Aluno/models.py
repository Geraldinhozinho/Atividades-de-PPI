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
    interesses = models.TextField()
    
    def __str__(self):
        return self.interesses
    

class Hobbies(models.Model):
    titulo = models.CharField(max_length=100)
    sobre = models.TextField()
    
    def __str__(self):
        return self.titulo

class Sobre (models.Model):
    email = models.EmailField()
    cidade = models.CharField(max_length=100)
    historia = models.TextField()
    
    def __str__(self):
        return self.email
    

class Amigos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    
    def __str__(self):
        return self.nome
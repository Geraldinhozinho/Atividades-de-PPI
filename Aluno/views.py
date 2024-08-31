from django.shortcuts import render
from .models import Aluno, Interesses, Hobbies, Sobre, Amigos
# Create your views here.

def index(request):
    alunos = Aluno.objects.all() # Select do django
    contexto = {
        'lista': alunos
    }
    return render(request, 'alunos/index.html',contexto)

def interesses(request):
    inter = Interesses.objects.all()
    contexto = {
        'lista1': inter
    }
    return render(request, 'alunos/interesses.html',contexto)

def gostos(request):
    gosto = Hobbies.objects.all()
    contexto = {
        'lista2': gosto
    }
    return render(request, 'alunos/hobbies.html',contexto)

def sobremim (request):
    eu = Sobre.objects.all()
    contexto = {
        'lista3': eu
    }
    return render(request, 'alunos/sobre.html',contexto)

def friends(request):
    amizade = Amigos.objects.all()
    contexto = {
        'lista4': amizade
    }
    return render(request, 'alunos/amigos.html',contexto)
from django.shortcuts import render
from .models import Aluno, Interesses
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

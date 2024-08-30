from django.shortcuts import render
from .models import Aluno
# Create your views here.

def index(request):
    alunos = Aluno.objects.all() # Select do django
    contexto = {
        'lista': alunos
    }
    return render(request, 'alunos/index.html',contexto)
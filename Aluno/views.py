from django.shortcuts import render
from .models import Aluno
# Create your views here.

def index(request):
    aluno = Aluno.objects.all() # Select do django
    contexto = {
        'lista': aluno,
    }
    return render(request, 'alunos/index.html',contexto)
from django.shortcuts import render
from .models import  Aluno

# Create your views here.
def index(request):
    alunos = Aluno.objects.all() # Select do django
    contexto = {
        'alunos': alunos,
    }
    return render(request, 'alunos/index.html',contexto)

def detalhe_aluno(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id) # Select do django
    contexto = {
        'aluno': aluno
    }
    return render(request, 'alunos/detalhe_aluno.html',contexto)
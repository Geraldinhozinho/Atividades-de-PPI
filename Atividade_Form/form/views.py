from django.shortcuts import render
from .forms import FormularioForm
# Create your views here.

def index(request):
    return render(request, 'forms/index.html')





def form(request):
    sucesso = False
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            # Processar os dados aqui (ex: salvar no banco de dados)
            sucesso = True
    else:
        form = FormularioForm()

    return render(request, 'forms/form.html', {'form': form, 'sucesso': sucesso})
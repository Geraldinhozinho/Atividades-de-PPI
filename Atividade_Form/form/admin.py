'''def form(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()  # Salva diretamente no banco de dados
            return ('sucesso')  # Redireciona para uma página de sucesso
    else:
        form = FormularioForm()

    return render(request, 'forms/form.html', {'form': form})'''
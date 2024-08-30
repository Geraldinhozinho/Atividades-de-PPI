from django.contrib import admin
from .models import Aluno, Interesses
# Register your models here.
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'idade', 'curso', 'altura'] 
    
@admin.register(Interesses)
class InteressesAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']
from django.contrib import admin
from .models import Aluno, Interesses, Hobbies,Sobre, Amigos
# Register your models here.
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'idade', 'curso', 'altura'] 
    
@admin.register(Interesses)
class InteressesAdmin(admin.ModelAdmin):
    list_display = ['nome', 'interesses']
    

@admin.register(Hobbies)
class HobbiesAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'sobre']
 
@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    list_display = ['email', 'cidade', 'historia']
    
@admin.register(Amigos)
class AmigosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']
    

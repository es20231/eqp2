from django import forms
from .models import Usuario

class FormularioDeCadastro(forms.ModelForm):
  class Meta:
    model = Usuario
    fields = ["nome_de_usuario", "nome_completo", "email", "senha",]
    labels = {'nome_de_usuario': "Nome de Usuário", "nome_completo": "Nome Completo", "email" : "Email", "senha" : "Senha",}
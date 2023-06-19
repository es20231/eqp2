from django.shortcuts import render
from .models import Usuario
from .formularios import FormularioDeCadastro

# Create your views here.
def listagem_de_usuarios(request):
    usuarios = Usuario.objects.all()
    contexto = {"usuarios" : usuarios}
    return render(request, "listagem_de_usuarios.html", contexto)

def cadastro_de_usuario(request):
    if request.method == "POST":
        formulario_de_cadastro = FormularioDeCadastro(request.POST)
        
        if formulario_de_cadastro.is_valid():
            formulario_de_cadastro.save()

    else:
        formulario_de_cadastro = FormularioDeCadastro()

    contexto = {"formulario_de_cadastro" : formulario_de_cadastro}

    return render(request, "cadastro_de_usuario.html", contexto)
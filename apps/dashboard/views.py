from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from autenticacao.forms import ProfileForm
from django.contrib import messages
from .models import Imagem
from post.models import Post

@login_required(login_url='/autenticacao/login/')
def dashboard(request):
    """Função que renderiza a página inicial do dashboard"""

    if request.method == "POST":
        imagem = Imagem()

        imagem.usuario = request.user
        imagem.imagem = request.FILES['acao']
        imagem.save()

        return redirect(dashboard)
        
    else:
        profile_form = ProfileForm(instance=request.user.profile)
        lista_imagens = Imagem.objects.filter(usuario=request.user)
        lista_posts = Post.objects.filter(usuario=request.user)
    

    return render(request, 'dashboard/dash.html', {'profile_form': profile_form, 'lista_imagens' : lista_imagens, 'lista_posts' : lista_posts})
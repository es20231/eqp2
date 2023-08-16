from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import Profile 
from .models import Imagem
from post.models import Post
import uuid

@login_required(login_url='/autenticacao/login/')
def dashboard(request):
    """Função que renderiza a página inicial do dashboard"""
        
    profile = Profile.objects.get(usuario=request.user)
    lista_imagens = Imagem.objects.filter(usuario=request.user)
    lista_posts = Post.objects.filter(usuario=request.user)

    contexto = {
        'profile': profile,
        'lista_imagens' : lista_imagens,
        'lista_posts' : lista_posts
    }

    return render(request, 'dashboard/dash.html', contexto)

def upload_imagem(request):
    """Função que faz o upload de imagens para a galeria do usuário"""

    for imagem in request.FILES.getlist('envio_galeria'):
        imagem_1 = Imagem(usuario=request.user, imagem=imagem)
        imagem_1.save()

    return redirect(dashboard)

def novo_post(request):
    imagem_id = request.POST.get('postar_imagem').strip()
    imagem_postar = Imagem.objects.get(id=uuid.UUID(imagem_id))
    return render(request, 'post/novo-post.html', {'imagem_postar': imagem_postar})

def detalhes_post(request):
    postagem_id = request.POST.get('visualizar_postagem').strip()
    visualizar_postagem = Post.objects.get(id=uuid.UUID(postagem_id))
    return render(request, 'post/detalhes-post.html', {'visualizar_postagem': visualizar_postagem})

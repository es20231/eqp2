from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import Profile
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Imagem
from post.models import Post
import uuid


@login_required(login_url='/autenticacao/login/')
def dashboard(request):
    """Função que renderiza a página inicial do dashboard"""

    profile = Profile.objects.get(usuario=request.user)
    lista_imagens = Imagem.objects.filter(usuario=request.user)
    lista_posts = Post.objects.filter(usuario=request.user)
    lista_usuarios_comuns = Profile.objects.filter(
        usuario__is_staff=False, usuario__is_superuser=False)

    contexto = {
        'profile': profile,
        'lista_imagens': lista_imagens,
        'lista_posts': lista_posts,
        'lista_usuarios': lista_usuarios_comuns
    }

    return render(request, 'dashboard/dash.html', contexto)


@login_required(login_url='/autenticacao/login/')
def visitar_perfil(request, username):
    """Função que renderiza a página de perfil de um usuário"""

    if username == request.user.username:
        return redirect(dashboard)

    profile = Profile.objects.get(usuario__username=username)
    lista_posts = Post.objects.filter(usuario__username=username)
    lista_usuarios_comuns = Profile.objects.filter(
        usuario__is_staff=False, usuario__is_superuser=False)

    contexto = {
        'profile': profile,
        'lista_posts': lista_posts,
        'lista_usuarios': lista_usuarios_comuns
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
    lista_likes = visualizar_postagem.likes.all()
    lista_dislikes = visualizar_postagem.dislikes.all()
    contexto = {
        'lista_likes': lista_likes,
        'lista_dislikes': lista_dislikes,
        'visualizar_postagem': visualizar_postagem
    }
    
    return render(request, 'post/detalhes-post.html', contexto)

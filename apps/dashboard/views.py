from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Imagem
from post.models import Post
import uuid

@login_required(login_url='/autenticacao/login/')
def dashboard(request):
    """Função que renderiza a página inicial do dashboard"""
        
    profile_form = ProfileForm(instance=request.user.profile)
    lista_imagens = Imagem.objects.filter(usuario=request.user)
    lista_posts = Post.objects.filter(usuario=request.user)

    contexto = {
        'profile_form': profile_form,
        'lista_imagens' : lista_imagens,
        'lista_posts' : lista_posts
    }

    return render(request, 'dashboard/dash.html', contexto)

def upload_imagem(request):
    imagem = Imagem(usuario=request.user, imagem=request.FILES['envio_galeria'])
    imagem.save()
    return redirect(dashboard)

def novo_post(request):
    imagem_id = request.POST.get('postar_imagem').strip()
    imagem_postar = Imagem.objects.get(id=uuid.UUID(imagem_id))
    return render(request, 'post/novo-post.html', {'imagem_postar': imagem_postar})

def detalhes_post(request):
    postagem_id = request.POST.get('visualizar_postagem').strip()
    visualizar_postagem = Post.objects.get(id=uuid.UUID(postagem_id))
    return render(request, 'post/detalhes-post.html', {'visualizar_postagem': visualizar_postagem})

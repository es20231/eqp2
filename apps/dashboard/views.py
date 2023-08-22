from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import Profile 
from .models import Imagem
from post.models import Post
import uuid

import os
import cv2
from .filtros import *
from .utils import *

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

# TODO: Cozinhar esse macarrão(refatorar)
def novo_post(request):
    filtro = request.POST.get('filtro')
    imagem_id = request.POST.get('postar_imagem').strip()
    imagem_postar = Imagem.objects.get(id=uuid.UUID(imagem_id))
    
    caminho_da_imagem_a_ser_mostrada = ""
   
    # Pega a URL da original
    if filtro == "original":
        caminho_da_imagem_a_ser_mostrada = "." + imagem_postar.imagem.url

    # aplica o filtro na cópia da original
    else:
        nome_da_imagem_com_filtro = especificar_filtro_no_nome_da_imagem(imagem_postar.imagem.url, filtro)
        caminho_relativo_da_original = "." + imagem_postar.imagem.url
        caminho_relativo_da_filtrada = "." + nome_da_imagem_com_filtro
        
        img_original = cv2.imread(caminho_relativo_da_original, cv2.IMREAD_COLOR)

        cv2.imwrite(caminho_relativo_da_filtrada, img_original)
        copia_da_imagem = cv2.imread(caminho_relativo_da_filtrada, cv2.IMREAD_COLOR)

        caminho_da_imagem_a_ser_mostrada = caminho_relativo_da_filtrada

        if filtro == "blur":
            filtro = FiltroBlur()

        elif filtro == "grayscale":
            filtro = FiltroGrayScale()

        elif filtro == "clahe":
            filtro = FiltroClahe()
        
        copia_da_imagem = filtro.aplicar_filtro(copia_da_imagem)
        cv2.imwrite(caminho_relativo_da_filtrada, copia_da_imagem)
        
    caminho_da_imagem_a_ser_mostrada = "../../" + caminho_da_imagem_a_ser_mostrada # ajeita o caminho que vai ser acessado no novo_post.html
                    
    return render(request, 'post/novo-post.html', {'imagem_postar': imagem_postar, "caminho_da_imagem_a_ser_mostrada" : caminho_da_imagem_a_ser_mostrada})

def detalhes_post(request):
    postagem_id = request.POST.get('visualizar_postagem').strip()
    visualizar_postagem = Post.objects.get(id=uuid.UUID(postagem_id))
    return render(request, 'post/detalhes-post.html', {'visualizar_postagem': visualizar_postagem})
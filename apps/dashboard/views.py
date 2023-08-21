from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import Profile 
from .models import Imagem
from post.models import Post
import uuid
import os
import cv2
from .filtros import *
#from ...SNAPture.settings import BASE_DIR

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
    #print(filtro)
    imagem_id = request.POST.get('postar_imagem').strip()
    imagem_postar = Imagem.objects.get(id=uuid.UUID(imagem_id))
    
    # Cria uma cópia da imagem, se não existir, para que os filtros não modifiquem a original. 
    nome_do_arquivo, extensao = imagem_postar.imagem.url.split(".")
    if not "(copia)" in nome_do_arquivo:
        nome_do_arquivo += "(copia)"
        caminho_da_copia = nome_do_arquivo + "." + extensao
        #caminho_da_original = os.path.join(BASE_DIR, imagem_postar.imagem.url) # Python não permite acessar pastas superiores para pegar o BASE_DIR
        #img = cv2.imread("/../.." + imagem_postar.imagem.url, cv2.IMREAD_COLOR) # Não é uma boa solução, pois o diretório atual não é uma info confiável.
        #print(img) # None. Imagem não encontrada. Problema: acertar o path da imagem correta
        #cv2.imwrite(BASE_DIR + caminho_da_copia, img) # Cria a cópia.
    
    else:
        caminho_da_copia = nome_do_arquivo + "." + extensao
    
    
    if filtro == "original":
        pass

    elif filtro == "blur":
        filtro = FiltroBlur()

    elif filtro == "grayscale":
        filtro = FiltroGrayScale()
        

    print(imagem_postar.imagem.url)
    return render(request, 'post/novo-post.html', {'imagem_postar': imagem_postar, "caminho_da_copia_da_imagem" : caminho_da_copia})

def detalhes_post(request):
    postagem_id = request.POST.get('visualizar_postagem').strip()
    visualizar_postagem = Post.objects.get(id=uuid.UUID(postagem_id))
    return render(request, 'post/detalhes-post.html', {'visualizar_postagem': visualizar_postagem})
from django.shortcuts import render, redirect
from .models import Post, Comentario
from dashboard.models import Imagem
from django.contrib.auth.decorators import login_required
from dashboard.views import dashboard

import os

@login_required(login_url='/autenticacao/login/')
def publicar(request, id):
    """Função que publica um post do usuário"""
    caminho_da_imagem_a_ser_salva = request.POST.get('caminho_da_imagem_a_ser_salva')
    caminho_da_imagem_a_ser_salva = caminho_da_imagem_a_ser_salva[6:]
    # Criar novo post;
    
    novo_post = Post()
    novo_post.imagem = caminho_da_imagem_a_ser_salva
    novo_post.usuario = request.user
    novo_post.descricao = request.POST.get('descricao')
    novo_post.save()    
    return redirect(dashboard)
    
@login_required(login_url='/autenticacao/login/')   
def remover(request, id):
    """Função que remove um post do usuário"""
    Post.objects.filter(id=id).delete()
    return render(request, 'dashboard/dash.html')

  
def dar_like(request, id):
    post = Post.objects.get(id=id)
    
    if request.method == 'POST':
        user = request.user
        if user not in post.likes.all() and user not in post.dislikes.all():
            post.likes.add(user)
            post.save()
    lista_likes = post.likes.all()
    lista_dislikes = post.dislikes.all()
    lista_comentarios = Comentario.objects.filter(id_post=id)

    contexto = {
        'lista_likes': lista_likes,
        'lista_dislikes': lista_dislikes,
        'lista_comentarios': lista_comentarios,
        'visualizar_postagem': post
    }
    return render(request, 'post/detalhes-post.html', contexto)

  
def dar_dislike(request, id):
    post = Post.objects.get(id=id)
    
    if request.method == 'POST':
        user = request.user
        if user not in post.likes.all() and user not in post.dislikes.all():
            post.dislikes.add(user)
            post.save()
    lista_likes = post.likes.all()
    lista_dislikes = post.dislikes.all()
    lista_comentarios = Comentario.objects.filter(id_post=id)

    contexto = {
        'lista_likes': lista_likes,
        'lista_dislikes': lista_dislikes,
        'lista_comentarios': lista_comentarios,
        'visualizar_postagem': post
    }
    return render(request, 'post/detalhes-post.html', contexto)

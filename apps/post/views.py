from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
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

@login_required(login_url='/autenticacao/login/')
def visualizar(request, id):
    """Função que visualiza um post do usuário"""
    objeto = Post.objects.get(id=id)
    return render(request, 'post/detalhes-post.html', {'post_form': objeto})

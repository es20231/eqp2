from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .models import Post

def publicar(request):
    """Função que publica um post do usuário"""
    if request.method =="GET":
        return render(request, 'novo_post.html')
    
    else:
        id_post = request.POST.get('id')
        imagem_post = request.FILES
        data_de_publicacao_post = request.POST.get('data_de_publicacao')

        if not imagem_post:
            messages.warning(request, 'É necessário uma imagem para fazer uma publicação')
            return redirect(publicar)
        
        #Criar novo post
        novo_post = Post()

        novo_post.id = id_post
        novo_post.imagem = imagem_post
        novo_post.data_de_publicacao = data_de_publicacao_post
        novo_post.save()

        return render(request, 'detalhes_post.html')
    
def remover(request, id):
    Post.objects.filter(id=id).delete()
    return render(request, '/')

def visualizar(request, id):
    context = {"id":id}
    return render(request, 'detalhes_post.html', context)

from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .forms import PostForm
from .models import Post

def publicar(request):
    """Função que publica um post do usuário"""
    if request.method =="GET":
        return render(request, 'novo-post.html')
    
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

        return render(request, 'detalhes-post.html')
    
def remover(request, id):
    Post.objects.filter(id=id).delete()
    return HttpResponse("registro deletado")

def visualizar(request, id):
    objeto = Post.objects.filter(id=id)
    return render(request, 'post/detalhes-post.html', {'post_form': objeto[0]})

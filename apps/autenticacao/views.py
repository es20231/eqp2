from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.shortcuts import redirect
from dashboard import views as dashboard_views

def cadastro(request):
    """Função que realiza o cadastro do usuário"""

    # Caso a requisição seja pra abrir a página de cadastro
    if request.method == "GET":
        return render(request, 'autenticacao/cadastro.html')
    
    # Caso a requisição seja envio do formulário de cadastro
    else:
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha_confirmada = request.POST.get('senha_confirmada')
        nome = request.POST.get('nome_completo')

        # Verifica se todos os campos foram preenchidos
        if any([not usuario, not email, not senha, not senha_confirmada, not nome]):
            return HttpResponse('Todos os campos são obrigatórios')

        # Verifica se o usuário já existe
        email_existe = User.objects.filter(email=email).exists()

        if email_existe:
            return HttpResponse('Email já cadastrado')
        
        else:
            if senha != senha_confirmada:
                return HttpResponse('Senhas não conferem')
            
            # Cria o usuário
            novo_usuario = User.objects.create_user(usuario, email, senha)

            # Adiciona o nome completo do usuário e salva
            nome_usuario_completo = nome.split(' ')
            novo_usuario.first_name = nome_usuario_completo[0]
            novo_usuario.last_name = ' '.join(nome_usuario_completo[1:])
            novo_usuario.save()

            return HttpResponse(novo_usuario.get_full_name())

def login(request):
    """Função que realiza o login do usuário"""

    if request.method == "GET":
        return render(request, 'autenticacao/login.html')
    
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Verifica se todos os campos foram preenchidos
        if any([not email, not senha]):
            return HttpResponse('Todos os campos são obrigatórios')
        
        # Como o Django não permite logar com email, precisamos pegar o username
        try:
            username = User.objects.get(email=email).username
            
            usuario = authenticate(request, username=username, password=senha)

            if usuario is not None:
                django_login(request, usuario)
            
                # Quando o usuário estiver logado, redireciona para a página de dashboard
                return redirect(dashboard_views.dashboard)

            else:
                return HttpResponse('Usuário ou senha inválidos')

        except User.DoesNotExist:
            return HttpResponse('Usuário ou senha inválidos')
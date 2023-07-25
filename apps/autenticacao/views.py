from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from dashboard import views as dashboard_views
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

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
            messages.warning(request, 'Todos os campos são obrigatórios')
            return redirect(cadastro)

        # Verifica se o usuário já existe
        email_existe = User.objects.filter(email=email).exists()

        if email_existe:
            messages.error(request, 'Email já cadastrado')
            return redirect(cadastro)
        
        else:
            if senha != senha_confirmada:
                messages.error(request, 'Senhas não conferem')
                return redirect(cadastro)
            
            # Cria o usuário
            novo_usuario = User.objects.create_user(usuario, email, senha)

            # Adiciona o nome completo do usuário e salva
            nome_usuario_completo = nome.split(' ')
            novo_usuario.first_name = nome_usuario_completo[0]
            novo_usuario.last_name = ' '.join(nome_usuario_completo[1:])
            novo_usuario.save()

            return redirect(login)

def login(request):
    """Função que realiza o login do usuário"""

    if request.method == "GET":
        return render(request, 'autenticacao/login.html')
    
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Verifica se todos os campos foram preenchidos
        if any([not email, not senha]):
            messages.warning(request, 'Todos os campos são obrigatórios')
            return redirect(login) 
        
        # Como o Django não permite logar com email, precisamos pegar o username
        try:
            username = User.objects.get(email=email).username
            
            usuario = authenticate(request, username=username, password=senha)

            if usuario is not None:
                django_login(request, usuario)


            
                # Quando o usuário estiver logado, redireciona para a página de dashboard
                return redirect(dashboard_views.dashboard)

            else:
                messages.error(request, 'Usuário ou senha inválidos')
                #return render(request, 'autenticacao/login.html')
                return redirect(login)
            
        except User.DoesNotExist:
            messages.error(request, 'Usuário ou senha inválidos')
            return redirect(login)

def logout(request):
    """Função que realiza o logout do usuário"""

    django_logout(request)
    return redirect(login)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Imagem

@login_required(login_url='/autenticacao/login/')
def dashboard(request):
    """Função que renderiza a página inicial do dashboard"""

    if request.method == "POST":
        imagem = Imagem()

        imagem.usuario = request.user
        imagem.imagem = request.FILES['acao']
        imagem.save()

        return redirect(dashboard)
        
    else:
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'dashboard/dash.html', {'profile_form': profile_form})
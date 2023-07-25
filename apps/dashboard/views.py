from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from autenticacao.forms import ProfileForm
from django.contrib import messages

@login_required(login_url='/autenticacao/login/')
def dashboard(request):
    """Função que renderiza a página inicial do dashboard"""

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Perfil atualizado com sucesso')
            return redirect(dashboard)
        
    else:
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'dashboard/dash.html', {'profile_form': profile_form})
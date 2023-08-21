from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileForm, PasswordUpdateForm
from django.shortcuts import redirect
from dashboard.views import dashboard

# Create your views here.
@login_required(login_url='/autenticacao/login/')
def update_user(request):
    """Função que atualiza o perfil do usuário"""

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()

        return redirect(dashboard)

    else:
        profile_form = ProfileForm(instance=request.user.profile)
        user_form = UserUpdateForm(instance=request.user)

        context = {
            'profile_form': profile_form,
            'user_form': user_form
        }

        return render(request, 'profile/atualizar-usuario.html', context)

@login_required(login_url='/autenticacao/login/')
def update_password(request):
    """Função que atualiza a senha do usuário"""

    if request.method == 'POST':
        password_form = PasswordUpdateForm(request.POST, instance=request.user)

        if password_form.is_valid():
            password_form.save()

        return redirect(dashboard)

    else:
        password_form = PasswordUpdateForm(instance=request.user)

        context = {
            'password_form': password_form,
        }

        return render(request, 'profile/atualizar-senha.html', context)
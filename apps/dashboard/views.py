from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/autenticacao/login/')
def dashboard(request):
    usuario = request.user.get_full_name()
    return HttpResponse(f'Bem vindo, {usuario}!')
    return render(request, 'dashboard/dashboard.html')
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from visitantes.forms import VisitanteForm, AutorizaVisitanteForm
from visitantes.models import Visitante

@login_required
def registrar_visitante(request):

    form = VisitanteForm()

    if request.method == "POST":
        form = VisitanteForm(request.POST, request.FILES)

        if form.is_valid():
            # Salva os dados do formulário no banco de dados, mas não faz o commit
            visitante = form.save(commit=False)

            # Define o campo "registrado_por" do visitante como o porteiro atualmente autenticado
            visitante.registrado_por = request.user.porteiro

            # Salva o visitante no banco de dados
            visitante.save()

            # Mensagem de sucesso gerada quando há um registro de visitante
            messages.success(
                request,
                "Visitante registrado com sucesso"
            )

            return redirect("index")

    # Cria um contexto contendo o nome da página e o formulário
    # Com o contexto se consegue utilizar o valor de cada chave diretamente no HTML
    context = {
        "nome_pagina" : "Registrar Visitante",
        "form" : form,
    }

    return render(request, "registrar_visitante.html", context)

@login_required
def informacoes_visitante(request, id):

    visitante = get_object_or_404(
        Visitante,
        id=id
    )

    form = AutorizaVisitanteForm()

    if request.method == "POST":
        form = AutorizaVisitanteForm(
            request.POST,
            instance=visitante # Informa ao django a atualização do visitante referente ao id com o corpo da requisição POST
        )

        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.status = "EM_VISITA"
            visitante.horario_autorizacao = timezone.now()

            visitante.save()

            messages.success(
                request,
                "Entrada de visitante autorizada com sucesso"
            )

            return redirect("index")

    context = {
        "nome_pagina": "Informações do visitante",
        "visitante": visitante,
        "form": form,
    }

    return render(request, "informacoes_visitante.html", context)

@login_required
def finalizar_visita(request, id):

    if request.method == 'POST':
        visitante = get_object_or_404(
            Visitante,
            id=id
        )

        visitante.status = "FINALIZADO"
        visitante.horario_saida = timezone.now()

        visitante.save()

        messages.success(
            request,
            "Visita finalizada com sucesso"
        )

        return redirect("index")

    else:
        return HttpResponseNotAllowed(
            ["POST"],
            "Método não permitido"
        )
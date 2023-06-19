from django.urls import path
from . import views

urlpatterns = [
    path("listagem_de_usuarios/", views.listagem_de_usuarios),
    path("cadastro_de_usuario/", views.cadastro_de_usuario)
]
from django.urls import path
from . import views

urlpatterns = [
    path('publicar/<uuid:id>', views.publicar, name='publicar_imagem'),
    path('remover/<uuid:id>', views.remover, name='remover_post'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('publicar/<uuid:id>', views.publicar, name='publicar_imagem'),
    path('remover/<uuid:id>', views.remover, name='remover_post'),
    path('like/<uuid:id>', views.dar_like, name='like_post'),
    path('dislike/<uuid:id>', views.dar_dislike, name='dislike_post'),
]
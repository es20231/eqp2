from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('upload_imagem/', views.upload_imagem, name='upload_imagem'),
    path('novo_post/', views.novo_post, name='novo_post'),
    path('detalhes_post/', views.detalhes_post, name='detalhes_post')
]
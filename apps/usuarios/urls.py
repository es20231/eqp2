from django.urls import path

from . import views

urlpatterns = [
    path('atualizar-usuario/', views.update_user, name='atualizar_usuario'),
]
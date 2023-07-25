from django.urls import path
from . import views

urlpatterns = [
    path('publicar/', views.publicar),
    path('<uuid:id>/remover/', views.remover),
    path('<uuid:id>/visualizar/', views.visualizar)
]
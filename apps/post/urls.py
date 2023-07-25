from django.urls import path
from . import views

urlpatterns = [
    path('publicar/', views.publicar),
    path('publicar2/', views.publicar2),
    path('<uuid:id>/remover/', views.remover),
    path('<uuid:id>/visualizar/', views.visualizar)
]
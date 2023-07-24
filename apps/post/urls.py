from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:id>/remover/', views.remover)
]
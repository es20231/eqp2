from django.db import models

class Usuario(models.Model):
    nome_de_usuario = models.CharField(max_length=20)
    nome_completo = models.CharField(max_length=50)
    email = models.CharField(max_length = 30)
    senha = models.CharField(max_length= 20)
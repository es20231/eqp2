from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_de_perfil = models.ImageField(upload_to='static/media/fotos_de_perfil', default='static/resources/default.jpg')
    descricao_de_perfil = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.usuario.get_full_name()
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"
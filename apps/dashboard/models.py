from django.db import models
import uuid
from django.contrib.auth.models import User

class Imagem(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    usuario = models.ForeignKey(User, on_delete= models.CASCADE)
    imagem = models.ImageField(upload_to="static/media/galeria", null=True, blank=True)

    def __UUID__(self): 
        return self.id
    
    class Meta:
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"
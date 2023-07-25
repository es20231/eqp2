from django.db import models
import uuid
from datetime import datetime
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Post(models.Model):
    def validate_size_value(arquivo):
        filesize = arquivo.size

        if filesize > 10 * 1024 * 1024:
            raise ValidationError("O tamanho máximo de Imagem é 10MB!")
        else:
            return arquivo
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    usuario = models.ForeignKey(User, on_delete= models.CASCADE)
    imagem = models.ImageField(upload_to='static/media', null=True, validators=[validate_size_value])
    descricao = models.TextField()
    data_de_publicacao = models.DateTimeField(default=datetime.now)

    def __UUID__(self):
        return self.id
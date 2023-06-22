from django.db import models

# Create your models here.
class Imagem(models.Model):
	imagem 		= models.ImageField(upload_to="imgs/", null=True, blank=True)
	descricao	= models.TextField(blank=True)
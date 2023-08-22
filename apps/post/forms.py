from django import forms 
from .models import Post, Comentario

class PostForm(forms.ModelForm): 
    class Meta: 
        model = Post 
        fields = ['id', 'imagem', 'descricao', 'data_de_publicacao'] 

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
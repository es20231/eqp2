from django import forms

from .models import Imagem

class ImagemForm(forms.ModelForm):
	class Meta:
		model = Imagem
		fields = [
			'imagem',
			'descricao'
		]
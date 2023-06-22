from django.shortcuts import render
from .models import Imagem
from .forms import ImagemForm

# Create your views here.
def upload_view(request, *args, **kwargs):
	form = ImagemForm(request.POST, request.FILES)
	
	if (request.method == "POST"):
		if form.is_valid():
			form.save()
			form = ImagemForm()

	context = {
		'form' : form
	}

	return render(request, "upload.html", context)

def listagem_view(request, *args, **kwargs):
	entradas = Imagem.objects.all()
	context = {
		'object_list' : entradas
	}
	return render(request, "listagem.html", context)

def homepage_view(request, *args, **kwargs):
	return render(request, "home.html", {})
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Profile
from post.models import Post


# Create your tests here.
class VisualizacaoFeedTest(TestCase):
	"""Teste para visualizacao de posts no feed usuário"""

	def setUp(self):
		self.cliente = Client()

	def test_login_feed(self):
		register_response = self.cliente.post('/autenticacao/cadastro/', {
            'nome_completo': 'Teste 1',
            'usuario': 'teste',
            'email': 'teste@teste.com',
            'senha': '123',
            'senha_confirmada': '123'
        }, follow=True)

		self.assertRedirects(register_response, '/autenticacao/login/')


		login_response = self.client.post('/autenticacao/login/', {
            'email': 'teste@teste.com',
            'senha': '123'
        })

		self.assertRedirects(login_response, '/')


		# Confere se a pagina de dashboard do novo usuario possui 0 posts
		pagina_dash = self.client.get("/")
		self.assertEqual(len(pagina_dash.context['lista_posts']), 0)



class FluxoPublicacaoFeedTest(TestCase):
	"""Teste para a publicacao e posterior visualizacao de posts no feed usuário"""

	def setUp(self):
		self.cliente = Client()

	def test_login_feed(self):
		register_response = self.cliente.post('/autenticacao/cadastro/', {
            'nome_completo': 'Teste 1',
            'usuario': 'teste',
            'email': 'teste@teste.com',
            'senha': '123',
            'senha_confirmada': '123'
        }, follow=True)

		self.assertRedirects(register_response, '/autenticacao/login/')


		login_response = self.client.post('/autenticacao/login/', {
            'email': 'teste@teste.com',
            'senha': '123'
        })

		self.assertRedirects(login_response, '/')


		# TODO:
		# Confere se a pagina de dashboard do novo usuario possui 0 posts
		# Cria uma imagem
		# Realiza o envio para a galeria usando o link + post request com a imagem
		# Verifica o status code da resposta
		# Verifica se a página de dashboard do usuário contem 1 post
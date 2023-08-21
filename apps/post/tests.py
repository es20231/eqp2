from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Post
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
import uuid

class PostTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_publicar(self):
        User.objects.create_user('test', 'teste@teste.com', 'test123')
        user = self.client.login(username='test', password='test123')

        with open('static/resources/lupa.png', 'rb') as imagem:
            teste_imagem = Post()
            teste_imagem.id = uuid.uuid4()
            teste_imagem.usuario = User.objects.get(username='test')
            teste_imagem.imagem = SimpleUploadedFile(imagem.name, imagem.read(), content_type='image/png')
            teste_imagem.descricao = 'Teste de publicação'
            teste_imagem.data_de_publicacao = timezone.now()
            teste_imagem.save()
        
        self.assertEqual(Post.objects.count(), 1)

class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_visualizar(self):
        User.objects.create_user('teste', 'teste@teste.com', 'test123')
        user = self.client.login(username='teste', password='test123')

        with open('static/resources/lupa.png', 'rb') as imagem:
            teste_imagem = Post()
            teste_imagem.id = uuid.uuid4()
            teste_imagem.usuario = User.objects.get(username='teste')
            teste_imagem.imagem = SimpleUploadedFile(imagem.name, imagem.read(), content_type='image/png')
            teste_imagem.descricao = 'Teste de publicação'
            teste_imagem.data_de_publicacao = timezone.now()
            teste_imagem.save()

        self.assertEqual(Post.objects.count(), 1)

        """
        objeto = Post.objects.get(id=teste_imagem.id)
        
        print(objeto.imagem.url)
        print(objeto.id)

        response = self.client.post('/novo_post', {'postar_imagem': objeto.id}, follow=True)

        print(response.content)
        
        self.assertEqual(response.status_code, 200)
        """

        # TODO:
        # Realizar um post request com a imagem criada para a galeria do usuario (mesmo fluxo do teste de dashboard)
        # Realizar um post request com o id da imagem criada para a view de novo_post
        # Realizar um post request com o id da imagem criada para a view de detalhes_post
        # Verificar o status code de cada request
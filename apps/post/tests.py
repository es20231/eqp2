from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Post
from django.core.files.uploadedfile import SimpleUploadedFile
import uuid

class PostTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_publicar(self):
        User.objects.create_user('test', 'teste@teste.com', 'test123')
        user = self.client.login(username='test', password='test123')

        with open('static/media/lupa.png', 'rb') as imagem:
            teste_imagem = Post()
            teste_imagem.id = uuid.uuid4()
            teste_imagem.usuario = User.objects.get(username='test')
            teste_imagem.imagem = SimpleUploadedFile(imagem.name, imagem.read(), content_type='image/png')
            teste_imagem.descricao = 'Teste de publicação'
            teste_imagem.save()

        
        self.assertEqual(Post.objects.count(), 1)

class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_visualizar(self):
        User.objects.create_user('teste', 'teste@teste.com', 'test123')
        user = self.client.login(username='teste', password='test123')

        with open('static/media/lupa.png', 'rb') as imagem:
            teste_imagem = Post()
            teste_imagem.id = uuid.uuid4()
            teste_imagem.usuario = User.objects.get(username='teste')
            teste_imagem.imagem = SimpleUploadedFile(imagem.name, imagem.read(), content_type='image/png')
            teste_imagem.descricao = 'Teste de publicação'
            teste_imagem.save()

        self.assertEqual(Post.objects.count(), 1)

        objeto = Post.objects.filter(id=teste_imagem.id)[0]
        
        response = self.client.get(f'/post/{objeto.id}/visualizar/', follow=True)

        self.assertEqual(response.status_code, 200)
from django.test import TestCase, Client
from django.contrib.auth.models import User

# Create your tests here.
class RegisterTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_cadastro(self):
        """Teste de cadastro de usuário"""

        # Teste de cadastro de usuário
        User.objects.create(username='usuario_teste', email='teste@teste.com', password='teste123')

        # Teste de recuperar usuário cadastrado
        usuario_cadastrado = User.objects.get(username='usuario_teste')
        self.assertTrue(usuario_cadastrado)

class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login(self):
        """Teste do fluxo de login de usuário"""

        register_response = self.client.post('/autenticacao/cadastro/', {
            'nome_completo': 'Usuario Teste 1',
            'usuario': 'usuario_teste',
            'email': 'usuarioteste@teste.com',
            'senha': 'teste123',
            'senha_confirmada': 'teste123'
        }, follow=True)

        # Teste de redirecionamento para a página de login após o cadastro
        self.assertRedirects(register_response, '/autenticacao/login/')
        self.assertTemplateUsed(register_response, 'autenticacao/login.html')

        login_response = self.client.post('/autenticacao/login/', {
            'email': 'usuarioteste@teste.com',
            'senha': 'teste123'
        })

        # Teste de redirecionamento para a página inicial após o login
        self.assertRedirects(login_response, '/')


class InvalidLoginTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login(self):
        """Teste de login inválido"""

        # Teste de login com email não cadastrado
        login_response = self.client.post('/autenticacao/login/', {
            'email': 'emailnaocadastrado@teste.com',
            'senha': 'invalida123'
        }, follow=True)	

        # Teste de redirecionamento para a página de login após o login inválido
        self.assertRedirects(login_response, '/autenticacao/login/')
        self.assertTemplateUsed(login_response, 'autenticacao/login.html')
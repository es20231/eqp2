# Testes da Aplicação

## Testes Unitários (TU)

### TU-01 Teste de unidade relativo à autenticação de usuário:
* TU-01-c1 Verifica se a tabela de usuários é criada corretamente no banco de dados.
* TU-01-c2 Verifica se o método test_cadastro está cadastrando usuários no BD corretamente.

### TU-02 Teste de unidade relativo ao dashboard da aplicação:
* TU-02-c1 Verifica se o método test_salvarImagem está salvando imagens no Dashboard do usuário.

### TU-03 Teste de unidade relativo aos posts da aplicação:
* TU-03-c1 Verifica se a tabela de posts é criada no banco de dados corretamente.
* TU-03-c2 Verifica se o método test_publicar está cadastrando posts.
* TU-03-c3 Verifica se o método test_visualizar está visualizando posts.

### TU-04 Teste de unidade relatvo ao feed da aplicação:
* TU-04-c1 Verifica se o método ___ está criando posts no Feed do usuário.

## Teste de Sistema (TS)

### TS-01 Casos de Testes para a autenticação de usuário

**TS-01-c1 Fluxo principal - Fluxo para logar com um usuário válido**

**Entradas:**
- Nome de usuário válido
- Senha válida

**Passos:**
- Acesse a página de login do usuário.
- Insira um nome de usuário válido.
- Insira uma senha válida.
- Pressione o botão de login.

**Resultado esperado:**
- O sistema deve autenticar com sucesso o usuário.
- O sistema deve redirecionar o usuário para a página de dashboard.

**TS-01-c2 Fluxo de exceção - Fluxo para logar com um usuário inválido**

**Entradas:**
- Nome de usuário inválido
- Senha inválida

**Passos:**
- Acesse a página de login do usuário.
- Insira um nome de usuário inválido.
- Insira uma senha inválida.
- Pressione o botão de login.

**Resultado esperado:**
- O sistema deve exibir uma mensagem de erro informando que as credenciais são inválidas.

### TS-02 Casos de Testes para o dashboard

**TS-02-c1 Fluxo principal - Fluxo para salvar uma imagem no Dashboard do usuário**

**Pré-condições:**

**Passos:**


**Resultado esperado:**

### TS-03 Casos de Testes para os posts

**TS-03-c1 Fluxo principal - Fluxo para visualizar um post no feed**

**Pré-condições:**

**Passos:**

**Resultado esperado:**

### TS-04 - Casos de teste para o feed

**TS-04-c1 Fluxo principal - Fluxo para postar uma imagem no Feed do usuário**

**Pré-condições:**

**Passos:**

**Resultado esperado:**
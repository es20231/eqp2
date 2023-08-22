# eqp2 - SNAPture
Um sistema de upload de fotos inspirado no Instagram.

![tela](https://github.com/es20231/eqp2/assets/62819962/625ca747-1e6d-48c9-9326-634225478d44)


# Como baixar
## Clone o repositório
```bash
git clone git@github.com:es20231/eqp2.git
```


## Dentro do projeto, crie um ambiente virtual
#### Windows
```bash
python -m venv .venv
```

#### Linux
```bash
python3 -m venv .venv
```


## Inicie o ambiente virtual
#### Windows
```bash
.venv/Scripts/activate
```

#### Linux
```bash
source .venv/bin/activate
```


## Instale os módulos necessários
#### Windows
```bash
pip install -r requirements.txt
```

#### Linux
```bash
pip3 install -r requirements.txt
```


## Faça as migrações e inicie o server
#### Windows
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

#### Linux
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```


# Equipe
Equipe 2 - ES 2023.1

* Ciro Olímpio de Melo
* Enzo Eduardo Cassiano Ibiapina
* Gabriel Alves da Silva
* Ingrid Miranda dos Santos
* João Pedro Monteiro da Silva Barros

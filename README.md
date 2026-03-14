# Blog Django

Projeto de blog desenvolvido durante o curso de Python do Luiz Otávio Miranda, usando Django.

## Sobre o projeto

Este repositório contém uma aplicação de blog com:

- páginas estáticas e posts;
- templates com layout base e componentes reutilizáveis;
- painel administrativo do Django;
- configuração de ambiente com Docker.

## Requisitos

Para rodar localmente sem Docker:

- Python 3.11+ (ou versão compatível com o `requirements.txt`);
- pip;
- ambiente virtual recomendado.

Para rodar com Docker:

- Docker;
- Docker Compose.

## Como executar com Docker

Na raiz do projeto, execute:

```bash
docker compose up --build
```

Depois, acesse no navegador:

- aplicação: `http://localhost:8000`
- admin: `http://localhost:8000/admin`

## Como executar localmente (sem Docker)

1. Crie e ative um ambiente virtual.
2. Instale as dependências.
3. Rode as migrações.
4. Inicie o servidor.

Exemplo no Windows (PowerShell), dentro da pasta `djangoapp`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Se houver conflito com Python global, use o executável do ambiente virtual diretamente:

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

## Estrutura principal

- `djangoapp/blog/`: app principal do blog (models, views, urls, templates e static);
- `djangoapp/site_setup/`: configurações de site e links de menu;
- `djangoapp/project/`: configurações globais do projeto Django;
- `scripts/`: scripts auxiliares para ambiente Docker;
- `dotenv_files/`: arquivos de variáveis de ambiente.

## Comandos úteis

Dentro de `djangoapp`:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Licença

Projeto de estudo para fins educacionais.
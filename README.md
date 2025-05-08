# Deise Santos Imóveis

Sistema web para gerenciamento de imóveis desenvolvido com Django.

## Requisitos

- Python 3.11+
- Django 5.2.1
- Outras dependências listadas em `requirements.txt`

## Configuração do Ambiente

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd deise_santos_imoveis
```

2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione as seguintes variáveis:
```
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
```

5. Execute as migrações:
```bash
python manage.py migrate
```

6. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

O site estará disponível em `http://127.0.0.1:8000/`

## Estrutura do Projeto

- `core/`: Configurações principais do projeto
- `imoveis/`: App para gerenciamento de imóveis
- `contato/`: App para formulário de contato
- `templates/`: Templates HTML
- `static/`: Arquivos estáticos (CSS, JS, imagens)
- `media/`: Arquivos de mídia enviados pelos usuários

## Funcionalidades

- Catálogo de imóveis
- Detalhes do imóvel
- Formulário de contato
- Área administrativa

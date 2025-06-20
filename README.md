# IAGO Multimarcas - Revenda de Carros

Sistema web para revenda de carros desenvolvido com Django.

## Requisitos

- Python 3.11+
- Django 5.2.1
- Outras dependências listadas em `requirements.txt`

## Configuração do Ambiente

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd revenda-carros
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
- `carros/`: App para gerenciamento de carros
- `contato/`: App para formulário de contato
- `templates/`: Templates HTML
- `static/`: Arquivos estáticos (CSS, JS, imagens)
- `media/`: Arquivos de mídia enviados pelos usuários

## Funcionalidades

- Catálogo de carros disponíveis para venda
- Detalhes do veículo (marca, modelo, ano, cor, portas, combustível, valor, etc.)
- Upload de fotos dos carros
- Formulário de contato para interessados
- Área administrativa para cadastro e edição de veículos

---

Desenvolvido para IAGO Multimarcas - Revenda de Carros

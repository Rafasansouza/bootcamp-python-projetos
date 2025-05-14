# CRUD com FastAPI, SQL ALchemy, pydantic, PostgreSQL, Docker e Streamlit.

Este projeto foi desenvolvido como parte do **Bootcamp de Python da Jornada de Dados** e demonstra a construção de um sistema CRUD completo, integrando:

- Backend com **FastAPI**
- Banco de dados **PostgreSQL**
- Frontend com **Streamlit**
- Orquestração com **Docker Compose**

---

## 📌 O que é CRUD?

CRUD é um acrônimo para **Create**, **Read**, **Update** e **Delete**, que representam as operações básicas em um banco de dados.

> Exemplo do dia a dia: Quando você acessa um site como Mercado Livre, o seu navegador está fazendo um **SELECT** no banco para mostrar os produtos. Ao cadastrar um item, um **INSERT** acontece, e por aí vai.

---

## ⚙️ Tecnologias utilizadas

### Backend

- **FastAPI** – Framework moderno para construção de APIs com Python.
- **Uvicorn** – Servidor ASGI leve e rápido.
- **SQLAlchemy** – ORM para abstração e comunicação com o banco de dados.
- **Pydantic** – Validação de dados e tipagem usando Python.

### Frontend

- **Streamlit** – Criação de interfaces web com Python.
- **Requests** – Requisições HTTP para consumir a API.
- **Pandas** – Manipulação e exibição de dados em tabela.

### Banco de Dados

- **PostgreSQL** – Banco de dados relacional open-source robusto.

---

## 🐳 Instalação com Docker

Execute o comando abaixo na raiz do projeto:

```bash
docker-compose up -d --build
```

---

## 🌐 Acesso

- **Frontend**: http://localhost:8501
- **Documentação da API** (Swagger): http://localhost:8000/docs

---

## 📁 Estrutura do projeto

```
├── README.md
├── docker-compose.yml
├── pyproject.toml
├── poetry.lock
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── router.py
│   └── requirements.txt
├── frontend/
│   ├── Dockerfile
│   └── app.py
```

---

## 🧠 Backend (FastAPI + SQLAlchemy + Pydantic)

### `database.py`
- Configura a conexão com o banco PostgreSQL via `create_engine`
- Cria `SessionLocal` para execução de queries
- Define a base `Base = declarative_base()` para os modelos

### `models.py`
- Define as tabelas do banco (ex: `Product`)
- Cada classe herda da `Base`
- Campos como `id`, `created_at` e `name` são definidos

### `schemas.py`
- Define os tipos de entrada/saída com **Pydantic**
- `ProductBase`, `ProductCreate`, `ProductUpdate`, `ProductResponse`

### `crud.py`
- Funções principais de CRUD com SQLAlchemy:
  - `create_product`, `get_product`, `get_products`, `update_product`, `delete_product`

### `router.py`
- Rotas da API REST:
  - `GET /products`
  - `GET /products/{id}`
  - `POST /products/`
  - `PUT /products/{id}`
  - `DELETE /products/{id}`

### `main.py`
- Inicializa o app FastAPI
- Inclui o roteador de produtos
- Uvicorn usado para servir a aplicação

---

## 💻 Frontend (Streamlit)

Interface simples em Python que consome a API:

- Formulário para cadastrar produto
- Lista produtos em tabela
- Permite editar e excluir produtos

### Bibliotecas:
- `streamlit`
- `requests`
- `pandas`

---

## 🐳 Docker Compose

### Serviços:

- **postgres**: banco de dados
- **backend**: FastAPI
- **frontend**: Streamlit

### Composição:

```yaml
services:
  postgres:
    image: postgres:latest
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: mydatabase
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
    networks:
      - mynetwork

  backend:
    build: ./backend
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    depends_on:
      - postgres
    environment:
      DATABASE_URL: postgresql://myuser:mypassword@postgres:5432/mydatabase
    networks:
      - mynetwork

  frontend:
    build: ./frontend
    volumes:
      - ./frontend:/app
    ports:
      - "8501:8501"
    networks:
      - mynetwork

networks:
  mynetwork:

volumes:
  postgres_data:
```

---

## 🚀 Preparado para Deploy na AWS ECS

### ECS (Elastic Container Service)
- Serviço de orquestração de containers
- Permite execução escalável de aplicações Docker

### ECS Fargate
- Executa containers **sem precisar gerenciar servidores**
- Ideal para microserviços e APIs leves como esta

### Componentes:
- **Cluster**: agrupa as máquinas (instâncias EC2 ou Fargate)
- **Task Definition**: especifica imagem Docker, CPU, memória etc.
- **Task**: execução de uma Task Definition
- **Service**: garante alta disponibilidade e escalabilidade

---

## 📷 Arquitetura do Projeto

> Para exibir uma imagem de arquitetura no seu README, salve a imagem no repositório (ex: `docs/arquitetura.png`) e use:

```markdown
![Arquitetura](docs/arquitetura.png)
```

---

## ✅ Conclusão

Este projeto proporciona:

- Um CRUD completo com API REST usando **FastAPI**
- Validação de dados com **Pydantic**
- Banco de dados relacional **PostgreSQL**
- Interface interativa com **Streamlit**
- Ambientes reprodutíveis com **Docker**
- Estrutura preparada para deploy com **AWS ECS**

---

## 📚 Créditos

Desenvolvido como parte do [Bootcamp de Python da Jornada de Dados](https://jornadadedados.com)

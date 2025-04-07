# NailURL

## Descrição do Projeto
**NailURL** é um encurtador de URLs simples desenvolvido com Flask e SQLAlchemy. Ele permite que os usuários insiram URLs longas e obtenham versões encurtadas que redirecionam para os links originais.

---

![showcase](src/nailurl0.gif)

---

## Funcionalidades
- Encurtar URLs longas.
- Redirecionar URLs encurtadas para os links originais.
- Interface simples e intuitiva.

---

## Tecnologias Utilizadas
- **Python** (Flask, Flask-SQLAlchemy)
- **PostgreSQL** (Banco de dados)
- **Docker** (Gerenciamento de contêineres)
- **HTML/CSS** (Interface do usuário)

---

## Como Executar o Projeto

1. **Pré-requisitos**:
   - Docker e Docker Compose instalados.

2. **Clone o repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd nailurl
   ```

3. **Configure as variáveis de ambiente**:
   Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   ```env
   POSTGRES_HOST=db
   POSTGRES_USER=seu_usuario
   POSTGRES_PASSWORD=sua_senha
   POSTGRES_DB=nailurl
   POSTGRES_PORT=5432
   ```

4. **Inicie os contêineres**:
   Construa e inicie os contêineres com:
   ```bash
   docker-compose up --build
   ```

5. **Acesse a aplicação**:
   - Acesse o navegador em: [http://localhost:5000](http://localhost:5000).

---

## Comandos Úteis

- **Executar em segundo plano**:
  ```bash
  docker-compose up -d --build
  ```

- **Parar os contêineres**:
  ```bash
  docker-compose down
  ```

- **Verificar logs**:
  ```bash
  docker-compose logs -f
  ```

- **Reconstruir apenas o serviço web**:
  ```bash
  docker-compose up -d --build web
  ```

---

## Estrutura do Projeto

```
nailurl/
├── app/
│   ├── main.py          # Código principal da aplicação Flask
│   ├── init_db.py       # Script para inicializar o banco de dados
│   ├── templates/       # Arquivos HTML
│   │   └── index.html   # Página inicial
├── Dockerfile           # Configuração do Docker
├── docker-compose.yml   # Configuração do Docker Compose
├── requirements.txt     # Dependências do projeto
├── .env                 # Variáveis de ambiente
└── README.md            # Documentação do projeto
```

---

## Contribuição
Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias no projeto.

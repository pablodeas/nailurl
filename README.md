Para iniciar sua aplicação com Docker após ter configurado seu Dockerfile e docker-compose.yml, siga estes passos:

1. Primeiro, certifique-se de estar no diretório do projeto que contém os arquivos Dockerfile e docker-compose.yml

2. Construa e inicie os contêineres com o comando:
   ```bash
   docker-compose up --build
   ```
   
   O parâmetro `--build` garante que a imagem da sua aplicação Flask seja construída antes de iniciar os contêineres. Isso é especialmente importante na primeira execução ou após fazer alterações no código.

3. Para executar os contêineres em segundo plano (modo detached):
   ```bash
   docker-compose up -d --build
   ```

4. Para verificar os logs da aplicação enquanto ela está rodando em modo detached:
   ```bash
   docker-compose logs -f
   ```
   
   Ou para ver apenas os logs de um serviço específico:
   ```bash
   docker-compose logs -f web
   ```

5. Para parar a aplicação:
   ```bash
   docker-compose down
   ```
   
   Se quiser remover os volumes também (cuidado, isso apagará os dados do banco):
   ```bash
   docker-compose down -v
   ```

Uma vez iniciados, sua aplicação Flask estará disponível na porta que você definiu (provavelmente 5000), e poderá acessá-la em http://localhost:5000 no seu navegador ou fazer requisições para essa URL.

O PostgreSQL estará rodando em um contêiner separado, e sua aplicação Flask se conectará a ele usando a string de conexão que você definiu na variável de ambiente DATABASE_URL.

Se precisar reconstruir apenas um serviço específico:
```bash
docker-compose up -d --build web
```

Para verificar o status dos contêineres em execução:
```bash
docker-compose ps
```
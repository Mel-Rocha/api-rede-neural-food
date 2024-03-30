## Dependências do projeto
### Ambiente virtual
Criar um ambiente virtual na raiz do projeto com o comando

```bash
python -m venv venv
```

### Instalar as dependências necessárias
Executar o comando para instalar as dependencias que estão em requirements.txt
```bash
pip install -r requirements.txt
```

---

## Variaveis de ambiente necessárias
### Banco de dados do precificador
- DATABASE_URL: Url de conexão com banco de dados do projeto

### Banco de dados da Tabela Somos
- PG_HOST_RETENTION: Host
- PG_PORT_RETENTION: Porta
- PG_USER_RETENTION: Usuário
- PG_PASSWORD_RETENTION: Senha
- DATABASE_RETENTION: Nome do banco de dados

---

## Rodar o projeto
Executar o comando a seguir na raiz do projeto

```bash
uvicorn main --reload
```

---

## Migrações no banco de dados
Se o projeto não possuir a pasta migrations ou essa pasta estiver vazia, executar o comando a seguir:

```bash
aerich init-db
```

Sempre que um modelo for alterado (campos foram acrescentados, alterados ou removidos), executar os comando a seguir 
para aplicar as mudanças no seu banco de dados.

Comando para gerar os arquivos de migração

```bash
aerich migrate
```

Comando para aplicar as migrações no banco de dados

```bash
aerich upgrade
```
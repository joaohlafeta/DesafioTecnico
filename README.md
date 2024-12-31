# MALO- Sistema de Gestão de Restaurante

Bem-vindo ao **MALO**, uma aplicação desenvolvida em Django e MySQL para gestão de restaurantes. Este sistema inclui funcionalidades de controle de pedidos, estoque e faturamento, além de gerenciamento de usuários.

## Funcionalidades

- **Controle de Pedidos:** Gerenciamento completo de pedidos realizados no restaurante.
- **Controle de Estoque:** Controle eficiente de entradas e saídas de produtos no estoque.
- **Faturamento:** Visualização e controle das finanças do restaurante.
- **Gerenciamento de Usuários:**
  - Dois tipos de usuários: **Garçom** e **Gerente**.
  - A primeira conta registrada será sempre de um gerente.
  - Gerentes podem criar novos usuários do tipo garçom.

## Tecnologias Utilizadas

- **Framework Backend:** Django.
- **Banco de Dados:** MySQL.
- **Containerização:** Docker.
  - **Dockerfile** e **docker-compose** para facilitar o deploy local.
- **Pipeline CI/CD:** GitHub Actions.
  - Verificação de vulnerabilidades no código utilizando SAST.
  - Testes automatizados de build.
  - Deploy automatizado na Google Cloud Platform (GCP).
- **Segurança:**
  - Utilização de variáveis de ambiente armazenadas em um arquivo `.env` para proteger informações sensíveis.
  - Segredos do GCP armazenados no **GitHub Secrets** para garantir a segurança durante o workflow de CI/CD.

## Deploy na GCP

A aplicação está configurada para realizar o deploy na **Google Cloud Platform**. Após o deploy, ela pode ser acessada via HTTP no endereço IP:

**http://34.59.212.245:8000**

## Rodando a Aplicação Localmente

### Pré-requisitos

Certifique-se de ter os seguintes arquivos e ferramentas:

- **Arquivos Necessários:**
  - `Dockerfile.local`
  - `docker-compose.local.yml`
  - `requirements.txt`
  - `espera.sh` (Para evitar que o DJango tente se conectar antes do Mysql estar em execução)
  - `.env` (com as configurações do banco de dados e variáveis de ambiente, será necessário que você crie de acordo com seu db local).

- **Ferramentas Necessárias:**
  - Docker instalado.

### Instruções

1. Clone este repositório para sua máquina local:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <PASTA_DO_REPOSITORIO>
   ```
   
2. Certifique-se de que o Docker está instalado e em execução.

3. Para iniciar a aplicação localmente, utilize o seguinte comando:

   ```bash
   docker-compose -f docker-compose.local.yml up --build  #adicionar -d caso queira rodar desacoplado
   ```

4. Após a execução, a aplicação estará disponível em:

   ```
   http://127.0.0.1:8000
   ```


## Estrutura do Projeto

- **Backend:** Django.
- **Banco de Dados:** MySQL.
- **Docker:** Facilita o deploy local e em ambientes de produção.
- **GitHub Actions:** Automatiza os pipelines de CI/CD e realiza verificações de vulnerabilidades.

## Segurança e Boas Práticas

- **Arquivo `.env`:** Todas as senhas e informações críticas estão armazenadas no `.env`.
- **GitHub Secrets:** Segredos da GCP estão configurados para garantir segurança durante o deploy.

Caso tenha dúvidas ou sugestões, entrar em contato com jhml@cesar.school


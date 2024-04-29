# Projeto-AWS
**Projeto Flask Dockerizado com MySQL e Integração com Amazon S3**

---
<img align="left" src="https://github.com/BiancaMalta/Projeto-AWS/assets/92928037/c0d9e407-524b-4963-ade3-5c6aa7d5f58a" width="60%" heigh="100%">

### Descrição do Projeto
Este projeto consiste em uma aplicação Flask dockerizada que utiliza um banco de dados MySQL para armazenar dados e integra-se com a Amazon S3 para armazenamento de arquivos. A aplicação permite o upload de arquivos, armazenamento de informações de relatórios no banco de dados e exibição dos relatórios enviados pelos usuários. Além disso, inclui uma função Lambda que é acionada por eventos do CloudWatch EventBridge para desligar a instância EC2.

### Estrutura do Projeto
O projeto é composto por cinco partes principais:</br> 


<img align="right" src="https://github.com/BiancaMalta/Projeto-AWS/assets/92928037/c0d07ab1-20f5-4bce-b1bf-9446b981f114"  width="50%">

1. **Aplicação Flask (Python)**:
   - Contém a lógica de negócios da aplicação, incluindo rotas, lógica de processamento de arquivos e interações com o banco de dados.
   - Hospedada em um contêiner Docker.
   - Responsável por servir páginas da web dinâmicas, lidar com solicitações HTTP e gerenciar o fluxo de dados.

2. **Banco de Dados MySQL**:
   - Armazena informações de relatórios enviados pelos usuários, como nome do arquivo e nome de usuário.
   - Hospedado em um contêiner Docker.
   - A aplicação Flask interage com este banco de dados para acessar e armazenar dados.

3. **EC2 Instance**:
   - Uma instância EC2 na AWS que hospeda a aplicação Flask e o banco de dados MySQL.
   - A instância EC2 está conectada ao bucket S3 para upload e download de arquivos.
   - Foi necessário alterar o grupo de segurança da instância EC2 para expor a porta 5000 e permitir o acesso de qualquer IP.
     
4. **Amazon S3 Bucket**:
   - Utilizado para armazenar arquivos enviados pelos usuários.
   - A aplicação Flask faz upload e download de arquivos para este bucket.

5. **Lambda Function**:
   - Uma função Lambda AWS que é acionada por eventos do CloudWatch EventBridge.
   - Responsável por desligar a instância EC2 em horários pré-determinados para reduzir custos operacionais.

![image](https://github.com/BiancaMalta/Projeto-AWS/assets/92928037/d697855b-8287-44ad-8545-494220586ff7)




### Como Executar o Projeto

1. **Pré-requisitos**:
   - Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.
   - Tenha as credenciais da Amazon S3 disponíveis para autenticação.
   - Configure a função Lambda e o CloudWatch EventBridge na AWS.
   - Crie uma Role no IAM com as permissões necessárias para acessar a Amazon S3, a instância EC2 e outros recursos relevantes.
   - Lembre-se de alterar o grupo de segurança da instância EC2.

2. **Configuração**:
   - Clone este repositório em sua máquina local.
   - Configure as variáveis de ambiente necessárias, como as credenciais da Amazon S3 e as configurações do MySQL, no arquivo `.env`.

3. **Execução**:
   - Abra um terminal na pasta raiz do projeto.
   - Execute o comando `docker-compose up` para construir e iniciar os contêineres da aplicação Flask e do banco de dados MySQL.
   - Configure e implante a função Lambda e o CloudWatch EventBridge na AWS.
   - Inicie a instância EC2 na AWS e altere o grupo de segurança para permitir o acesso na porta 5000 de qualquer IP.

4. **Utilização**:
   - Faça login na aplicação Flask com as credenciais de administrador (padrão: username=admin, password=admin).
   - Faça upload de arquivos através da interface da aplicação.
   - Visualize e gerencie os relatórios enviados pelos usuários.
   - Observe o agendamento e desligamento automático da instância EC2 pela função Lambda.

### Documentações Importantes:

1. [Documentação do Flask](https://flask.palletsprojects.com/)
2. [Documentação do MySQL](https://dev.mysql.com/doc/)
3. [Documentação do Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html)
4. [Documentação do Docker](https://docs.docker.com/)
5. [Documentação do Docker Compose](https://docs.docker.com/compose/)
6. [Documentação da AWS EC2](https://docs.aws.amazon.com/ec2/)
7. [Documentação da AWS Lambda](https://docs.aws.amazon.com/lambda/)
8. [Documentação do AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
9. [Documentação do AWS EventBridge (CloudWatch Events)](https://docs.aws.amazon.com/eventbridge/)

### Ferramentas Utilizadas
- **Figma**: Utilizado para prototipagem e design da interface da aplicação.
- **Docker e Docker Compose:** Proporcionou um ambiente de desenvolvimento e implantação consistente e portátil.
- **AWS:** Garantiu uma escalabilidade, automação, durabilidade e facilidade de integração.
- **Git:** Utilizado para gerenciar e controlar as versões do código-fonte.
- **Visual Studio Code (VSCode):** Excelente suporte para linguagens de programação como Python e SQL, o que facilitou o desenvolvimento, depuração e manutenção do código-fonte do projeto.

### Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas.


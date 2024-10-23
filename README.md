
# email-service-uber

O projeto consiste na resolução de um processo seletivo do Uber - Back-end track - no qual era solicitado que se criasse um dos quatro projetos e o escolhido foi o Email Service. 

# O que foi solicitado na descrição do processo

Foi solicitado pelos organizadores do processo que no projeto Email Service fosse cirado um serviço que aceitasse algumas informações necessárias e enviasse e-mails. O serviço deveria prover uma abstração entre dois servidores de e-mails caso um dos servidores tivesse algum erro, de forma que não aja problemas para os consumidores. 

Foram sugeridos 4 serviços e os escolhidos foram o Amazon SES e o Twilio Sendgrid, devido a grande utilização do Amazon SES no mercado e também pela praticidade vista no Sendgrid para disparo de e-mails. 

# Tecnologias e bibliotecas utilizadas

Para criar o projeto conforme foi solicitado, foi utilizado a linguagem Python com o uso de um ambiente venv com as bibliotecas abaixo que foram necessárias para o funcionamento adequado:

* annotated-types    0.7.0
* anyio              4.6.2.post1
* boto3              1.35.46
* botocore           1.35.46
* click              8.1.7
* colorama           0.4.6
* fastapi            0.115.2
* h11                0.14.0
* idna               3.10
* iniconfig          2.0.0
* jmespath           1.0.1
* packaging          24.1
* pip                24.2
* pluggy             1.5.0
* pydantic           2.9.2
* pydantic_core      2.23.4
* pytest             8.3.3
* python-dateutil    2.9.0.post0
* python-dotenv      1.0.1
* python-http-client 3.3.7
* s3transfer         0.10.3
* sendgrid           6.11.0
* six                1.16.0
* sniffio            1.3.1
* starkbank-ecdsa    2.2.0
* starlette          0.40.0
* typing_extensions  4.12.2
* urllib3            2.2.3
* uvicorn            0.32.0

Como mencionado, também foram utilizados dois provedores de e-mails: Amazon SES e Twilio SendGrid.

# Desafios

No desenvolvimento do projeto, existiram alguns desafios. Eles foram obstáculos que tiveram que ser contornados para o funcionamento correto de acordo com o que foi solicitado. 

Durante o processo de criação do primeiro serviço de provedor, Amazon SES, um dos desafios foi a decisão entre seguir com o SMTP ou com o AWS SDK(BOTO3 para Python), pois ambos servem para o envio de e-mails, porém o AWS SDK tem melhor controle de erros e templates e possui integração com o SES.

Dessa forma, pensando que o serviço estaria sendo desenvolvido para uma empresa de grande porte, foi utilizado o desenvolvimento com a AWS SDK. Isso exigiu mais desenvolvimento em python para criar toda a conexão com os sistemas da Amazon.

Outro desafio foi a escolha da arquitetura e a escolhida foi a Clean (Clean architecture) proposta por Robert C. Martin (Uncle Bob), no qual temos uma arquitetura em que os módulos ou entidades (entities) não são afetados por problemas ou erros nas APIs e/ou servidores de e-mails, por exemplo. 

Isso foi pensando tanto para a característica sugerida pelos desenvolvedores do processo seletivo, pois pediram uma arquitetura baseada em cliente/serviços, como também para facilitar a implementação do segundo servidor de e-mail que tem a função de disparo quando o primeiro falhar.





# Documentação da API

## Api relativa ao e-mail enviados

#### Envia e-mail:
### Função: send_mail()

```http
  POST /users/
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `to_email`      | `string` | **Obrigatório**. E-mail destinatário|
| `subject`      | `string` | **Obrigatório**. O assunto do e-mail |
| `body`      | `string` | **Obrigatório**. O corpo do e-mail |


# Rodando os testes

Para rodar os testes, rode o seguinte comando

```bash
  pytest
```


# Referência

 - [Uber - coding-challenge-tools](https://github.com/uber-archive/coding-challenge-tools)

- [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

- [Clean Architecture: A Craftsman's Guide to Software Structure and Design (Robert C. Martin Series)](https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164)

- [Welcome to botocore](https://botocore.amazonaws.com/v1/documentation/api/latest/index.html)

- [SendGrid](https://sendgrid.com/en-us)

- [Amazon SES](https://aws.amazon.com/pt/ses/)

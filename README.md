
# email-service-uber

This project was developed as part of a technical challenge for Uber - Back-end track. The task was to implement one of four proposed services, and the chosen one was the Email Service.

# Challenge Requirements

The objective was to create an email service capable of receiving necessary information and sending emails. Additionally, the system had to abstract two email providers to ensure reliability—automatically switching to a secondary provider if the primary one failed.

The selected email providers were Amazon SES and Twilio SendGrid, chosen for their industry adoption and ease of use.

# Technologies and Libraries Used

The project was built using Python within a venv environment, utilizing the following libraries:

* boto3 1.35.46
* fastapi 0.115.2
* pydantic 2.9.2
* pytest 8.3.3
* uvicorn 0.32.0

Additionally, Amazon SES and Twilio SendGrid were integrated as the email providers.

# Challenges Faced

## Email Provider Selection

One challenge was choosing between using SMTPlib or AWS SDK (Boto3) for Amazon SES. The AWS SDK was preferred due to its enhanced error handling, templating support, and seamless SES integration.

## Architecture

The project follows the Clean Architecture approach, as proposed by Robert C. Martin (Uncle Bob). This design ensures that core business logic remains independent of APIs or email providers, aligning with the client-service architecture suggested in the challenge. This also simplified the implementation of a fallback email provider.

# Documentação da API

## Send Email
```http
  POST /users/
```

| Parameter   | Type       | Description                                   |
| :---------- | :--------- | :------------------------------------------ |
| `to_email`      | `string` | **Required.** Recipient email |
| `subject`      | `string` | **Required.** Email subject |
| `body`      | `string` | **Required.** Email content |


# Running Tests

To run tests, execute:

```bash
  pytest
```


# References

 - [Uber - coding-challenge-tools](https://github.com/uber-archive/coding-challenge-tools)

- [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

- [Clean Architecture: A Craftsman's Guide to Software Structure and Design (Robert C. Martin Series)](https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164)

- [Welcome to botocore](https://botocore.amazonaws.com/v1/documentation/api/latest/index.html)

- [SendGrid](https://sendgrid.com/en-us)

- [Amazon SES](https://aws.amazon.com/pt/ses/)

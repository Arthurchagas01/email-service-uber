
from infrastructure.email_provider_2 import EmailProvider2
from domain.email_entity import Email


def test_send_email_to_client1():
    mock_email = Email('EMAIL', 'TESTE', 'teste1')
    sender = 'EMAIL'
    provider1 = EmailProvider2(sender)
    response = provider1.send_email(mock_email)

    assert response.status_code == 202
    

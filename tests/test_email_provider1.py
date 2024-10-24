import moto
import pytest
from infrastructure.email_provider_1 import EmailProvider1
from domain.email_entity import Email
import boto3

@pytest.fixture
def ses_v1():
    with moto.mock_ses():
        yield boto3.client('ses', region_name='us-east-2')

@pytest.fixture
def ses_v2():
    ses_v1.verify_domain_identity(Domain='email.com')
    with moto.mock_sesv2():
        yield
        
def test_send_email_to_client():
    mock_email = Email('EMAIL', 'TESTE', 'teste1')
    sender = 'EMAIL'
    provider = EmailProvider1(sender)
    response = provider.send_email(mock_email)

    assert response == 200
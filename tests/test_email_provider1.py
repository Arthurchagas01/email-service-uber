import pytest
from infrastructure.email_provider_1 import EmailProvider1
from unittest.mock import patch
from infrastructure.email_failover_service import EmailFailoverService
from application.send_email import SendEmail
from adapters.email_controller import EmailController

@patch('boto3.client')
def test_send_email_success(mock_boto_client):
    mock_client = mock_boto_client.return_value
    mock_client.send_email.return_value = {"MessageId": "12345"}
    
    provider = EmailProvider1("email destino")
    with pytest.raises(Exception) as exc_info:
        failover_service = EmailFailoverService()
        usecase = SendEmail(failover_service)
        controller = EmailController(usecase)
        
        response = controller.send_email(
        "Teste",
        "email destino",
        "Email de teste"
        )
    mock_client.send_email.assert_called_once()
    
    # Verifica o retorno da função
    assert response["MessageId"] == "12345"

# Teste para verificar tratamento de erro ao falhar o envio

@patch('boto3.client')
def test_send_email_failure(mock_boto_client):
    mock_client = mock_boto_client.return_value
    mock_client.send_email.side_effect = Exception("SES failed")
    
    #provider = EmailProvider1("email destino")
    
    with pytest.raises(Exception) as exc_info:
        failover_service = EmailFailoverService()
        usecase = SendEmail(failover_service)
        controller = EmailController(usecase)
        
        controller.send_email(
        "Teste",
        "email destino",
        "Email de teste"
        )
    
    assert str(exc_info.value) == "SES failed"

from infrastructure.email_failover_service import EmailFailoverService
from application.send_email import SendEmail
from adapters.email_controller import EmailController

if __name__ == '__main__':
    failover_service = EmailFailoverService()
    usecase = SendEmail(failover_service)
    controller = EmailController(usecase)
    
    controller.send_email('EMAIL SENDER', 'teste', 'Body')
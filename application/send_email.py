from domain.email_entity import Email
from infrastructure.email_failover_service import EmailFailoverService

class SendEmail:
    
    def __init__(self, failover_service: EmailFailoverService):
        self.failover_service  = failover_service
        
    def execute(self, email: Email):
        self.failover_service.send(email)
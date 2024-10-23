from application.send_email import SendEmail
from domain.email_entity import Email

class EmailController:
    def __init__(self, usecase: SendEmail):
        self.usecase = usecase
        
    def send_email(self, to_email, subject, body):
        email = Email(to_email, subject, body)
        self.usecase.execute(email)
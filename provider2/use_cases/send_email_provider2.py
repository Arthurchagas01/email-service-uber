from entities.email_entity import Email
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

class SendEmailWithSendGrid:
    def __init__(self):
        self.sender = "arthurchagas01@gmail.com"
        load_dotenv()         
        self.SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
        self.sg = SendGridAPIClient(self.SENDGRID_API_KEY)
    
    def SendWithSendGrid(self, email: Email):
        
        message = Mail(
            from_email=self.sender,
            to_emails=email.to_email,
            subject=email.subject,
            html_content=email.body
            )
        
        try:
            response = self.sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
            return response
        except Exception as e:
            print(e.message)
            return e
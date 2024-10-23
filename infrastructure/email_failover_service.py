from infrastructure.email_provider_1 import EmailProvider1
from infrastructure.email_provider_2 import EmailProvider2


class EmailFailoverService:
    def __init__(self):

        self.primary_provider = EmailProvider1(sender="EMAIL SENDER")
        self.secondary_provider = EmailProvider2(sender="EMAIL SENDER")
        
    def send(self, email):
        try:
            self.primary_provider.send_email(email)
        except:
            self.secondary_provider.send_email(email)
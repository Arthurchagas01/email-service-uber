from use_cases.send_email_provider1 import SendEmailWithAWS
from entities.email_entity import Email

class EmailController:
    def __init__(self, usecase: SendEmailWithAWS):
        self.usecase = usecase
        
    async def send_email(self, email):
        response = await self.usecase.sendWithAWS(email)
        return response
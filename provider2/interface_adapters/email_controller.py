from use_cases.send_email_provider2 import SendEmailWithSendGrid
from entities.email_entity import Email

class EmailController:
    def __init__(self, usecase: SendEmailWithSendGrid):
        self.usecase = usecase
        
    async def send_email(self, email):
        response = await self.usecase.SendWithSendGrid(email)
        return response
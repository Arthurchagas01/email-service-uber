from use_cases.send_email import SendEmail
from entities.email_entity import Email
import json

class EmailController:
    def __init__(self, usecase: SendEmail):
        self.usecase = usecase
        
    async def send_email(self, email):
        response = await self.usecase.execute(email)
        return response
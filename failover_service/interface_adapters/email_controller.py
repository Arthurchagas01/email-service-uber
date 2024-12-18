from use_cases.failover_use_case import Failover_use_case
from entities.email_entity import Email
import json

class EmailController:
    def __init__(self, usecase: Failover_use_case):
        self.usecase = usecase
        
    async def send_email(self, information):   
        response = await self.usecase.send_email(information)
        return response

    
   
   
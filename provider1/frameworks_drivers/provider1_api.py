from entities.email_entity import Email
from use_cases.send_email_provider1 import SendEmailWithAWS
from fastapi import APIRouter, HTTPException
from interface_adapters.email_controller import EmailController
import httpx
from pydantic import BaseModel 

router = APIRouter()

provider1_useCase = SendEmailWithAWS()
controller = EmailController(provider1_useCase)

class Information(BaseModel):
    to_email: str
    subject: str
    body: str

@router.post("/",  response_model=None)
async def provider1_service(information: Information):
    try:
        result = await controller.send_email(information)
        return result
    except httpx.HTTPStatusError as exc:
        if exc.response.status_code == 422:
            raise HTTPException(status_code=422, detail=exc.response.json())
        raise HTTPException(status_code=500, detail=f"Failed to send email: {exc}")
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {exc}")
from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from interface_adapters.email_controller import EmailController
from use_cases.send_email import SendEmail
import httpx

router = APIRouter()

class EmailRequest(BaseModel):
    to_email: str
    subject: str
    body: str
    
usecase = SendEmail()
controller = EmailController(usecase)

@router.post("/send-mail")
async def send_mail(email_request: EmailRequest):
    try:
        response = await controller.send_email(email_request)
        return response
    except httpx.HTTPStatusError as exc:
        if exc.response.status_code == 422:
            raise HTTPException(status_code=422, detail=exc.response.json())
        raise HTTPException(status_code=500, detail=f"Failed to proceed: {exc}")
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {exc}")
from entities.email_entity import Email
from use_cases.failover_use_case import Failover_use_case
from fastapi import APIRouter, HTTPException
from interface_adapters.email_controller import EmailController
import httpx
from pydantic import BaseModel 

router = APIRouter()

failover_use_case = Failover_use_case()
controller = EmailController(failover_use_case)

class Information(BaseModel):
    to_email: str
    subject: str
    body: str

@router.post("/",  response_model=None)
async def failover_system(information: Information):
    try:
        result = await controller.send_email(information)
        return result
    except httpx.HTTPStatusError as exc:
        if exc.response.status_code == 422:
            raise HTTPException(status_code=422, detail=exc.response.json())
        raise HTTPException(status_code=500, detail=f"Failed to send email: {exc}")
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {exc}")
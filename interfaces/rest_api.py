from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from adapters.email_controller import EmailController
from application.send_email import SendEmail
from infrastructure.email_failover_service import EmailFailoverService

app = FastAPI()

class EmailRequest(BaseModel):
    to_email: str
    subject: str
    body: str
    
failover_service = EmailFailoverService()
usecase = SendEmail(failover_service)
controller = EmailController(usecase)

@app.post("/send-mail")
async def send_mail(email_request: EmailRequest):
    try:
        controller.send_email(email_request.to_email, email_request.subject, email_request.body)
        return {"status": "success", "message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")
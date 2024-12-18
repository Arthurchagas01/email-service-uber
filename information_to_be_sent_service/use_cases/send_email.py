import httpx
from fastapi import HTTPException


class SendEmail:
      
    async def execute(self, email):
        
        failover_service_url = "http://127.0.0.1:8001/failover/"
        
        async with httpx.AsyncClient() as client:
            
            try:
                response = await client.post(failover_service_url, json=email.dict())
                return response.json()
            except httpx.HTTPStatusError as exc:
                if exc.response.status_code == 422:
                    raise HTTPException(status_code=422, detail=exc.response.json())
                raise HTTPException(status_code=500, detail=f"Failed to send email: {exc}")
            except Exception as exc:
                raise HTTPException(status_code=500, detail=f"Internal Server Error: {exc}")
                
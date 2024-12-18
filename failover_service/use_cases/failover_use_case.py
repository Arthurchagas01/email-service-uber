import httpx
from fastapi import HTTPException

class Failover_use_case():

    async def send_email(self, email):
        
        provider1_service_url = "http://127.0.0.1:8002/provider_1_email_service/"
 
        async with httpx.AsyncClient() as client:
            
            try:
                response = await client.post(provider1_service_url, json=email.dict())
                return response.json()
            except httpx.HTTPStatusError as exc:
                if exc.response.status_code == 422:
                    raise HTTPException(status_code=422, detail=exc.response.json())
                raise HTTPException(status_code=500, detail=f"Failed to call provider AWS: {exc}")
            except Exception as exc:
                raise HTTPException(status_code=500, detail=f"Internal Server Error: {exc}")   
            
    # async def send_email(self, email):
        
    #     provider2_service_url = "http://127.0.0.1:8003/provider_2_email_service/"
 
    #     async with httpx.AsyncClient() as client:
            
    #         try:
    #             response = await client.post(provider2_service_url, json=email.dict())
    #             return response.json()
    #         except httpx.HTTPStatusError as exc:
    #             if exc.response.status_code == 422:
    #                 raise HTTPException(status_code=422, detail=exc.response.json())
    #             raise HTTPException(status_code=500, detail=f"Failed to call provider AWS: {exc}")
    #         except Exception as exc:
    #             raise HTTPException(status_code=500, detail=f"Internal Server Error: {exc}")   
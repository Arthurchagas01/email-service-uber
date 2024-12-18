from frameworks_drivers import provider1_api
from fastapi import FastAPI

app = FastAPI()
app.include_router(provider1_api.router, prefix="/provider_1_email_service")
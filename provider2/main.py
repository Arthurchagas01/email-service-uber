from frameworks_drivers import provider2_api
from fastapi import FastAPI

app = FastAPI()
app.include_router(provider2_api.router, prefix="/provider_2_email_service")
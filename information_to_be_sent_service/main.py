from frameworks_drivers import rest_api
from fastapi import FastAPI

app = FastAPI()

app.include_router(rest_api.router, prefix="/email")
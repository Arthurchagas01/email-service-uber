from frameworks_drivers import failover_api
from fastapi import FastAPI

app = FastAPI()
app.include_router(failover_api.router, prefix="/failover")
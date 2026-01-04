from fastapi import FastAPI
from backend.app.api.routes import router

app = FastAPI(title="DCPT-64 Anomaly MVP")
app.include_router(router)

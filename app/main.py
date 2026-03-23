from fastapi import FastAPI
from api.v1.api import api_router

app = FastAPI(
    title='KFTC Onboarding',
    version="1.0.0",
    docs_url="/docs"
)

app.include_router(api_router, prefix="/api/v1")
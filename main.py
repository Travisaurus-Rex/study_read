from fastapi import FastAPI
from app.routes import health
from app.core.config import settings

app = FastAPI(title=settings.app_name)
app.include_router(health.router)

@app.get("/")
def read_root():
    return{ "message": f"{settings.app_name} is running!"}
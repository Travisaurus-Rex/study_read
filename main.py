from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routes import health, tts
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base

app = FastAPI(title=settings.app_name)
app.include_router(health.router)
app.include_router(tts.router)

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

@app.get("/")
def read_root():
    return{ "message": f"{settings.app_name} is running!"}
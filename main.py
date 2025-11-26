from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routes import health, tts
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables ON startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Close DB connection ON shutdown
    await engine.dispose()

# ❗ This is the line that was missing
app = FastAPI(title=settings.app_name, lifespan=lifespan)

app.include_router(health.router)
app.include_router(tts.router)

@app.get("/")
def read_root():
    return {"message": f"{settings.app_name} is running!"}

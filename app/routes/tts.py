from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.repositories import tts_repo 

router = APIRouter(prefix="/tts", tags=["tts"])

@router.get("/")
async def list_tts_jobs(db: AsyncSession = Depends(get_db)):
    jobs = await tts_repo.get_all_tts_jobs(db)
    return [
        {
            "id": j.id,
            "text": j.text,
            "provider": j.provider,
            "created_at": j.created_at
        }
        for j in jobs
    ]

@router.post("/")
async def create_tts_job(text: str, voice_id: str | None, provider: str | None, db: AsyncSession = Depends(get_db)):
    job = await tts_repo.create_tts_job(db, text, voice_id, provider)
    return {"id": job.id, "text": job.text, "created_at": job.created_at}
